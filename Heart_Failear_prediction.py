import pickle
heart_failear = pickle.load(open('Heart_Failear_prediction.pickle','rb'))
age = float(input('Age : '))
anaemia = input('Decrease of red blood cells or hemoglobin (y\\n): ').lower()
if anaemia == 'y' or anaemia == 'yes': anaemia_b = 1
else:anaemia_b = 0 
creatinine_phosphokinase = float(input('Level of the CPK enzyme in the blood (mcg/L) : '))
diabetes = input('If the patient has diabetes (y\\n): ').lower()
if diabetes == 'y' or diabetes == 'yes': diabetes_b = 1
else:diabetes_b = 0
ejection_fraction = float(input('Percentage of blood leaving the heart at each contraction (percentage) : '))
high_blood_pressure = input('If the patient has hypertension (y\\n): ').lower()
if high_blood_pressure == 'y' or high_blood_pressure == 'yes': high_blood_pressure_b = 1
else:high_blood_pressure_b = 0
platelets = float(input('Platelets in the blood (kiloplatelets/mL) : '))
serum_creatinine = float(input('Level of serum creatinine in the blood (mg/dL) : '))
serum_sodium = float(input(' Level of serum sodium in the blood (mEq/L) : '))
sex = input('sex (w\\m) : ').lower()
if sex == 'w' or sex == 'woman': sex_b = 0
else:sex_b = 1
smoking = input('If the patient smokes (y\\n): ').lower()
if smoking == 'y' or smoking == 'yes': smoking_b = 1
else:smoking_b = 0
time = float(input('Follow-up period (days) : '))
ans = heart_failear.predict([[age,anaemia_b,creatinine_phosphokinase,diabetes_b,ejection_fraction,high_blood_pressure_b,platelets,serum_creatinine,serum_sodium,sex_b,smoking_b,time]])
if ans[0] == 1: print(f'DEATH EVENT : Yes')
else:print(f'DEATH EVENT : No')
