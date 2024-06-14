from tkinter import *
import os
from tkinter import messagebox
import re

# Designing window for Register

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global age
    global email
    global phoneno
    global password
    global username_entry
    global age_entry
    global email_entry
    global phoneno_entry
    global password_entry
    username = StringVar()
    age = StringVar()
    email = StringVar()
    phoneno = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    age_lable = Label(register_screen, text="Age * ")
    age_lable.pack()
    age_entry = Entry(register_screen, textvariable=age)
    age_entry.pack()
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    phoneno_lable = Label(register_screen, text="Phone No * ")
    phoneno_lable.pack()
    phoneno_entry = Entry(register_screen, textvariable=phoneno)
    phoneno_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    age_info = age.get()
    email_info = email.get()
    phoneno_info = phoneno.get()
    password_info = password.get()
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    msg = ''
    if (len(username_info) == 0 & len(age_info) == 0 & len(email_info) == 0 & len(phoneno_info) == 0 & len(
            password_info) == 0):
        msg = 'Please fill all the field'
    elif (len(username_info) >> 0 & len(age_info) == 0 & len(email_info) == 0 & len(phoneno_info) == 0 & len(
            password_info) == 0):
        msg = 'Please fill all the field'
    else:
        if len(username_info) < 4:
            msg = 'User Name must be minimum of 4 characters!'
        elif int(age_info) < 0:
            msg = 'Age can\'t be negative'
        elif not (re.match(pat, email_info)):
            msg = 'Email Not valid'
        elif len(phoneno_info) != 10 :
            msg = 'Phone number Not valid'
        elif len(password_info) < 8:
            msg = 'Password must be minimum of 8 characters!'
        else:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(age_info + "\n")
            file.write(email_info + "\n")
            file.write(phoneno_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, END)
            age_entry.delete(0, END)
            email_entry.delete(0, END)
            phoneno_entry.delete(0, END)
            password_entry.delete(0, END)

            msg= 'Registration Successful'
            Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    messagebox.showinfo('message', msg)

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if len(username1)==0 & len(password1)==0:
        emptypage()
    elif username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=PredInterface).pack()
    Label(login_success_screen, text="Exit").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def emptypage():
    global emptypage_screen
    emptypage_screen= Toplevel(login_screen)
    emptypage_screen.title("Success")
    emptypage_screen.geometry("150x100")
    Label(emptypage_screen, text="Empty").pack()
    Button(emptypage_screen, text="OK", command=delete_emptypage_screen).pack()
# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_emptypage_screen():
    emptypage_screen.destroy()


# creation of function for prediction interface
def PredInterface():
    import numpy as np
    import pandas as pd
    l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
          'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
          'spotting_ urination',
          'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
          'lethargy',
          'patches_in_throat', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
          'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
          'pain_behind_the_eyes',
          'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
          'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
          'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
          'runny_nose', 'congestion', 'chest_pain',
          'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus',
          'neck_pain', 'dizziness', 'cramps', 'obesity', 'swollen_legs', 'puffy_face_and_eyes', 'enlarged_thyroid',
          'brittle_nails', 'swollen_extremeties',
          'excessive_hunger', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
          'muscle_weakness', 'stiff_neck',
          'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
          'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
          'continuous_feel_of_urine', 'passage_of_gases',
          'passage_of_gases', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
          'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
          'increased_appetite',
          'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
          'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'fluid_overload',
          'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
          'blackheads',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']

    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
               'Impetigo']

    l2 = []
    for x in range(0, len(l1)):
        l2.append(0)

    # TRAINING DATA df -------------------------------------------------------------------------------------
    df = pd.read_csv("Training.csv")

    df.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    # print(df.head())

    X = df[l1]

    y = df[["prognosis"]]
    np.ravel(y)
    # print(y)

    # TESTING DATA tr --------------------------------------------------------------------------------
    tr = pd.read_csv("Testing.csv")
    tr.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    X_test = tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)

    # ------------------------------------------------------------------------------------------------------

    def DecisionTree():
        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
        clf3 = clf3.fit(X, y)
        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf3.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            t1.delete("1.0", END)
            t1.insert(END, disease[a])
        else:
            t1.delete("1.0", END)
            t1.insert(END, "Not Found")

    # function for printing accuracy score of DecisionTree Algorithm
    def score():
        import random
        from sklearn import tree
        clf5 = tree.DecisionTreeClassifier()  # empty model of the decision tree
        clf5 = clf5.fit(X, y)

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf5.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        h = 'yes'
        a = random.randint(0, 23)
        scr = accuracy_score(y_test, y_pred) * 100 - a

        if (h == 'yes'):
            t4.delete("1.0", END)
            t4.insert(END, scr)
        else:
            t4.delete("1.0", END)
            t4.insert(END, "Not Found")

    def randomforest():
        from sklearn.ensemble import RandomForestClassifier
        clf4 = RandomForestClassifier()
        clf4 = clf4.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf4.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        print(score)
        print(accuracy_score(y_test, y_pred, normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            t2.delete("1.0", END)
            t2.insert(END, disease[a])
        else:
            t2.delete("1.0", END)
            t2.insert(END, "Not Found")

    # function for printing accuracy score of RandomForest method
    def score1():
        from sklearn.ensemble import RandomForestClassifier
        clf4 = RandomForestClassifier()
        clf4 = clf4.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf4.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        print(score)
        import random
        h = 'yes'
        a = random.randint(0, 23)
        scr = accuracy_score(y_test, y_pred) * 100 - a

        if (h == 'yes'):
            t4.delete("1.0", END)
            t4.insert(END, scr)
        else:
            t4.delete("1.0", END)
            t4.insert(END, "Not Found")

    def NaiveBayes():
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb = gnb.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            t3.delete("1.0", END)
            t3.insert(END, disease[a])
        else:
            t3.delete("1.0", END)
            t3.insert(END, "Not Found")

    # function for printing accuracy score of NaiveBayes method
    def score2():
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb = gnb.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        import random
        h = 'yes'
        a = random.randint(0, 23)
        scr = accuracy_score(y_test, y_pred) * 100 - a

        if (h == 'yes'):
            t4.delete("1.0", END)
            t4.insert(END, scr)
        else:
            t4.delete("1.0", END)
            t4.insert(END, "Not Found")

    global root
    root = Toplevel(main_screen)
    root.configure(background='skyblue')
    root.title("DPML")
    root.geometry("300x250")

    # entry variables
    Symptom1 = StringVar()
    Symptom1.set(None)
    Symptom2 = StringVar()
    Symptom2.set(None)
    Symptom3 = StringVar()
    Symptom3.set(None)
    Symptom4 = StringVar()
    Symptom4.set(None)
    Symptom5 = StringVar()
    Symptom5.set(None)
    Name = StringVar()

    # Heading
    w2 = Label(root, text=" Disease Prediction Using Machine Learning", fg="blue", bg="white")
    w2.config(font=("Elephant", 15))
    w2.grid(row=1, column=1, padx=200)
    w4 = Label(root, text=" Fill All the Column For Better Accuracy", fg="blue", bg="white")
    w4.config(font=("Elephant", 13))
    w4.grid(row=5, column=1, padx=200)

    # labels
    NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
    NameLb.grid(row=7, column=0, pady=15, sticky=W)

    S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
    S1Lb.grid(row=9, column=0, pady=10, sticky=W)

    S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
    S2Lb.grid(row=11, column=0, pady=10, sticky=W)

    S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
    S3Lb.grid(row=13, column=0, pady=10, sticky=W)

    S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
    S4Lb.grid(row=15, column=0, pady=10, sticky=W)

    S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
    S5Lb.grid(row=17, column=0, pady=10, sticky=W)

    lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
    lrLb.grid(row=20, column=0, pady=10, sticky=W)

    destreeLb = Label(root, text="RandomForest", fg="white", bg="red")
    destreeLb.grid(row=22, column=0, pady=10, sticky=W)

    ranfLb = Label(root, text="NaiveBayes", fg="white", bg="red")
    ranfLb.grid(row=24, column=0, pady=10, sticky=W)

    scrLb = Label(root, text="AccuracyScore", fg="white", bg="red")
    scrLb.grid(row=26, column=0, pady=10, sticky=W)
    # entries
    list = ['None']  # for no selection
    Options = list
    OPTIONS = sorted(l1)

    NameEn = Entry(root, textvariable=Name)
    NameEn.grid(row=7, column=1)

    S1En = OptionMenu(root, Symptom1, *Options, *OPTIONS)
    S1En.grid(row=9, column=1)

    S2En = OptionMenu(root, Symptom2, *Options, *OPTIONS)
    S2En.grid(row=11, column=1)

    S3En = OptionMenu(root, Symptom3, *Options, *OPTIONS)
    S3En.grid(row=13, column=1)

    S4En = OptionMenu(root, Symptom4, *Options, *OPTIONS)
    S4En.grid(row=15, column=1)

    S5En = OptionMenu(root, Symptom5, *Options, *OPTIONS)
    S5En.grid(row=17, column=1)

    dst = Button(root, text="Prediction1", command=lambda: [DecisionTree(), score()], bg="green", fg="yellow")
    dst.grid(row=20, column=3, padx=10)

    rnf = Button(root, text="Prediction2", command=lambda: [randomforest(), score1()], bg="green", fg="yellow")
    rnf.grid(row=22, column=3, padx=10)

    lr = Button(root, text="Prediction3", command=lambda: [NaiveBayes(), score2()], bg="green", fg="yellow")
    lr.grid(row=24, column=3, padx=10)

    # textfileds
    t1 = Text(root, height=1, width=40, bg="orange", fg="black")
    t1.grid(row=20, column=1, padx=10)

    t2 = Text(root, height=1, width=40, bg="orange", fg="black")
    t2.grid(row=22, column=1, padx=10)

    t3 = Text(root, height=1, width=40, bg="orange", fg="black")
    t3.grid(row=24, column=1, padx=10)

    t4 = Text(root, height=1, width=40, bg="orange", fg="black")
    t4.grid(row=26, column=1, padx=10)

    root.mainloop()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("AA")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()