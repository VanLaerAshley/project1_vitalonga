from time import sleep
sleep(20)
from flask import Flask, render_template, request
from DBClass import DbClass
from DCmotorClass import OpenCapsuleTray
from servomotor import keuzeMaken, aanzetten, volume
from stepperClass import StepperHall


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<start>')
def homeStart(start):
    aanzetten(start)
    return render_template('index.html')

@app.route('/koffie')
def koffiemain():
    return render_template('koffie.html')

@app.route('/koffie/sluitVerluchting')
def koffieSluitVerluchting():
    capsuleTray = OpenCapsuleTray(5, 6)
    capsuleTray.servoAirClose()
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    return render_template('koffie.html')



@app.route('/<start>/koffie')
def koffiestart(start):
    aanzetten(start)
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    return render_template('koffie.html')



@app.route('/keuzeCapsule/lungo')
def capsuleKeuzelungo(lungo=None):
    db = DbClass()
    capsule = db.chosenCapsules()
    return render_template('keuzeCapsuleL.html', Capsules=capsule), lungo

@app.route('/keuzeCapsule/espresso')
def capsuleKeuzeespresso(espresso=None):
    db = DbClass()
    capsule = db.chosenCapsules()
    return render_template('keuzeCapsuleE.html', Capsules=capsule), espresso


@app.route('/gekozenCapsuleLungo/<lungo>/<capsulenaam>')
def capsuleGekozenLungo(capsulenaam, lungo=None):
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    instantie.keuzeKoffie(capsulenaam)

    capsuleTray = OpenCapsuleTray(5, 6)
    capsuleTray.turnOffMotors()
    capsuleTray.runSequence()

    keuzeMaken(keuze=lungo)

    db = DbClass()
    capsule = db.chosenCapsule(capsulenaam)

    # klep openen om de warme dampen van de machine door te laten.
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    instantie.keuzeKoffie("5")
    capsuleTray = OpenCapsuleTray(5,6)
    capsuleTray.turnOffMotors()
    capsuleTray.servoAirOpen()


    return render_template('bereiding.html', Capsules=capsule)


@app.route('/gekozenCapsuleeEspresso/<espresso>/<capsulenaam>')
def capsuleGekozenEspresso(capsulenaam, espresso=None):
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    instantie.keuzeKoffie(capsulenaam)

    capsuleTray = OpenCapsuleTray(5,6)
    capsuleTray.turnOffMotors()
    capsuleTray.runSequence()

    keuzeMaken(keuze=espresso)

    db = DbClass()
    capsule = db.chosenCapsule(capsulenaam)

    #klep openen om de warme dampen van de machine door te laten.
    instantie = StepperHall([22, 23, 24, 25], 27)
    instantie.steps()
    instantie.waitTime()
    instantie.stepperToHall()
    instantie.keuzeKoffie("5")
    capsuleTray = OpenCapsuleTray(5,6)
    capsuleTray.turnOffMotors()
    capsuleTray.servoAirOpen()

    return render_template('bereiding.html', Capsules=capsule)



@app.route('/veranderenCapsules')
def capsulesVeranderen():
    db = DbClass()
    capsule = db.getCapsules()
    return render_template('capsulesVeranderen.html', Capsules=capsule)

@app.route('/veranderenCapsules/changed', methods=['POST'])
def capsulesVeranderen_post():
    keuze1 = request.form['rij1']
    keuze2 = request.form['rij2']
    keuze3 = request.form['rij3']
    keuze4 = request.form['rij4']
    db = DbClass()
    nieuweCapsules = db.storeCapsules(keuze1, keuze2, keuze3, keuze4)
    capsule = db.getCapsules()
    return render_template('capsulesVeranderen.html', Capsules=capsule), nieuweCapsules





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
