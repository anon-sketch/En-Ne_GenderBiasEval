import nltk
from tqdm import tqdm
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support


def evaluate_biasness(translated_file, original_file):
    with open(translated_file, 'r') as inputfile, open(original_file, 'r') as label_file:
        sentences = inputfile.readlines()
        golds = label_file.readlines()
        gold_labels = [each_gold.split(';')[-1].strip() for each_gold in golds]

    translated_labels = []
    m = 0
    f = 0
    both = 0
    neul = 0
    for i, s in enumerate(tqdm(sentences)):
        tokens = nltk.word_tokenize(s.strip().lower())

        if ('he' in tokens and 'she' in tokens) or (('him' in tokens or 'his' in tokens) and 'her' in tokens):
            print(i, s)
            user_label = str(input("Enter 'b' or 'y' or 'n': ")) #happens rarely
            if user_label == 'y':
                translated_labels.append(gold_labels[i])
            elif user_label == 'n':
                label = 'male' if gold_labels[i] == 'female' else 'female'
                translated_labels.append(label)
            elif user_label == 'b':
                translated_labels.append(gold_labels[i])
                both += 1
            else:
                translated_labels.append(gold_labels[i])

        elif 'she' in tokens or 'her' in tokens:
            translated_labels.append('female')

        elif 'he' in tokens or 'him' in tokens or 'his' in tokens:
            translated_labels.append('male')

        else:
            print(s)
            translated_labels.append(gold_labels[i])
            neul+=1
            if gold_labels[i] == 'male':
                m+=1
            else :
                f+=1

    print("Count:", len(sentences))
    print("No of both", both, both/len(sentences)*100)
    print("No of neutral sentences : ", neul)
    print("Percentage neutral",neul/len(sentences)*100 )
    print()
    print("Out of neutral sentences, no of actually male : ", m)
    print("Percentage neutral actually male", m/neul*100)
    print()
    print("Out of neutral sentences, no of actually female : ", f)
    print("Percentage neutral actually female", f/neul*100)

    return gold_labels, translated_labels


def calculate_metrices(anti_golds, anti_preds, pro_golds, pro_preds):
    # Accuracy
    ground_truth_labels = anti_golds + pro_golds
    predicted_labels = anti_preds + pro_preds

    accuracy = accuracy_score(ground_truth_labels, predicted_labels)
    print("Acc Percentage")
    print(accuracy*100)

    # F1 Scores
    _, _, f1_score_male, _ = precision_recall_fscore_support(ground_truth_labels, predicted_labels, average=None, labels=['male'])
    print("f1 for male : ", f1_score_male[0])
    _, _, f1_score_female, _ = precision_recall_fscore_support(ground_truth_labels, predicted_labels, average=None, labels=['female'])
    print("f1 for female : ", f1_score_female[0])

    print("delta G measure : ", f1_score_male[0]  - f1_score_female[0])


    # Macro F1 for anti
    _, _, f1_score_male, _ = precision_recall_fscore_support(anti_golds, anti_preds, average=None, labels=['male'])
    _, _, f1_score_female, _ = precision_recall_fscore_support(anti_golds, anti_preds, average=None, labels=['female'])
    macro_f1_anti = (f1_score_male[0] + f1_score_female[0])/2*100
    print(f"Macro-Averaged F1 Score for Anti-Stereotypical Sentences: {macro_f1_anti:.2f}")

    # Macro F1 for pro
    _, _, f1_score_male, _ = precision_recall_fscore_support(pro_golds, pro_preds, average=None, labels=['male'])
    _, _, f1_score_female, _ = precision_recall_fscore_support(pro_golds, pro_preds, average=None, labels=['female'])
    macro_f1_pro = (f1_score_male[0] + f1_score_female[0])/2*100
    print(f"Macro-Averaged F1 Score for Pro-Stereotypical Sentences: {macro_f1_pro:.2f}")

    print("Del S : ", macro_f1_anti - macro_f1_pro)



if __name__ == "__main__":
    # For polite
    print("##### Polite #####")
    print("\n Anti \n")
    anti_golds, anti_preds = evaluate_biasness('en_corpus_from_ne/gpt4o/en_anti.txt', 'ne_anti.txt')
    print("\n Pro \n")
    pro_golds, pro_preds = evaluate_biasness('en_corpus_from_ne/gpt4o/en_pro.txt', 'ne_pro.txt')
    calculate_metrices(anti_golds, anti_preds, pro_golds, pro_preds)

    # For informal
    print("\n\n\n##### Informal #####")
    print("\n Anti \n")
    anti_golds, anti_preds = evaluate_biasness('en_corpus_from_ne/gpt4o/en_anti_informal.txt', 'ne_anti_informal.txt')
    print("\n Pro \n")
    pro_golds, pro_preds = evaluate_biasness('en_corpus_from_ne/gpt4o/en_pro_informal.txt', 'ne_pro_informal.txt')
    calculate_metrices(anti_golds, anti_preds, pro_golds, pro_preds)


## IndicTrans2

# Count: 1497
# No of both 15 1.002004008016032
# No of neutral sentences :  73
# Percentage neutral 4.876419505678023

# Out of neutral sentences, no of actually male :  37
# Percentage neutral actually male 50.68493150684932

# Out of neutral sentences, no of actually female :  36
# Percentage neutral actually female 49.31506849315068

# Count: 1496
# No of both 13 0.8689839572192514
# No of neutral sentences :  62
# Percentage neutral 4.144385026737968

# Out of neutral sentences, no of actually male :  35
# Percentage neutral actually male 56.451612903225815

# Out of neutral sentences, no of actually female :  27
# Percentage neutral actually female 43.54838709677419
# Acc Percentage
# 61.476779151353156
# f1 for male :  0.6967167501391207
# f1 for female :  0.5210456357997342
# delta G measure :  0.17567111433938654
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 55.46
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 66.36
# Del S :  -10.904795123683463



# Count: 1497
# No of both 31 2.070808283233133
# No of neutral sentences :  81
# Percentage neutral 5.410821643286573

# Out of neutral sentences, no of actually male :  43
# Percentage neutral actually male 53.086419753086425

# Out of neutral sentences, no of actually female :  38
# Percentage neutral actually female 46.913580246913575

# Count: 1496
# No of both 20 1.3368983957219251
# No of neutral sentences :  70
# Percentage neutral 4.679144385026738

# Out of neutral sentences, no of actually male :  39
# Percentage neutral actually male 55.714285714285715

# Out of neutral sentences, no of actually female :  31
# Percentage neutral actually female 44.285714285714285
# Acc Percentage
# 51.68727029736051
# f1 for male :  0.6684324584637611
# f1 for female :  0.18906064209274673
# delta G measure :  0.47937181637101434
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 41.12
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 44.62
# Del S :  -3.495725607695128








#### Google

# Count: 1497
# No of both 0
# No of neutral sentences :  64
# Percentage neutral 4.275217100868404

# Out of neutral sentences, no of actually male :  35
# Percentage neutral actually male 54.6875

# Out of neutral sentences, no of actually female :  29
# Percentage neutral actually female 45.3125
# Count: 1496
# No of both 0
# No of neutral sentences :  59
# Percentage neutral 3.943850267379679

# Out of neutral sentences, no of actually male :  36
# Percentage neutral actually male 61.016949152542374

# Out of neutral sentences, no of actually female :  23
# Percentage neutral actually female 38.983050847457626
# Acc Percentage
# 61.176077514199804
# f1 for male :  0.65527950310559
# f1 for female :  0.5872115020809686
# delta G measure :  0.0680680010246214
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 52.77
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 71.42
# Del S :  -18.64856170791883




# Count: 1497
# No of both 1
# No of neutral sentences :  61
# Percentage neutral 4.074816299265197

# Out of neutral sentences, no of actually male :  32
# Percentage neutral actually male 52.459016393442624

# Out of neutral sentences, no of actually female :  29
# Percentage neutral actually female 47.540983606557376

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  56
# Percentage neutral 3.7433155080213902

# Out of neutral sentences, no of actually male :  33
# Percentage neutral actually male 58.92857142857143

# Out of neutral sentences, no of actually female :  23
# Percentage neutral actually female 41.07142857142857
# Acc Percentage
# 57.66789174741063
# f1 for male :  0.6867749419953596
# f1 for female :  0.39597989949748746
# delta G measure :  0.29079504249787214
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 49.98
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 58.36
# Del S :  -8.38294790181346



## GPT4o
# Count: 1497
# No of both 0 0.0
# No of neutral sentences :  366
# Percentage neutral 24.448897795591183

# Out of neutral sentences, no of actually male :  230
# Percentage neutral actually male 62.841530054644814

# Out of neutral sentences, no of actually female :  136
# Percentage neutral actually female 37.15846994535519

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  333
# Percentage neutral 22.259358288770052

# Out of neutral sentences, no of actually male :  160
# Percentage neutral actually male 48.048048048048045

# Out of neutral sentences, no of actually female :  173
# Percentage neutral actually female 51.95195195195195
# Acc Percentage
# 48.045439358503174
# f1 for male :  0.5429200293470287
# f1 for female :  0.5450995704802811
# delta G measure :  -0.0021795411332524717
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 40.93
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 67.22
# Del S :  -26.289111744182506

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  333
# Percentage neutral 22.259358288770052

# Out of neutral sentences, no of actually male :  160
# Percentage neutral actually male 48.048048048048045

# Out of neutral sentences, no of actually female :  173
# Percentage neutral actually female 51.95195195195195
# Acc Percentage
# 48.045439358503174
# f1 for male :  0.5429200293470287
# f1 for female :  0.5450995704802811
# delta G measure :  -0.0021795411332524717
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 40.93
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 67.22
# Del S :  -26.289111744182506


# Count: 1497
# No of both 1 0.06680026720106881
# No of neutral sentences :  279
# Percentage neutral 18.637274549098194

# Out of neutral sentences, no of actually male :  168
# Percentage neutral actually male 60.215053763440864

# Out of neutral sentences, no of actually female :  111
# Percentage neutral actually female 39.784946236559136

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  264
# Percentage neutral 17.647058823529413

# Out of neutral sentences, no of actually male :  119
# Percentage neutral actually male 45.07575757575758

# Out of neutral sentences, no of actually female :  145
# Percentage neutral actually female 54.92424242424242
# Acc Percentage
# 49.94988306047444
# f1 for male :  0.6342756183745583
# f1 for female :  0.40840254030288226
# delta G measure :  0.225873078071676
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 42.95
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 61.30
# Del S :  -18.352117810228194


# If neutral removed

# Acc Percentage
# 71.36652188439693
# f1 for male :  0.7248796147672553
# f1 for female :  0.7014977359804946
# delta G measure :  0.02338187878676068
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 60.45
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 82.18
# Del S :  -21.723280325895423

# Acc Percentage
# 68.09221516872704
# f1 for male :  0.7407005158837904
# f1 for female :  0.5853234910985671
# delta G measure :  0.1553770247852233
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 57.76
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 74.77
# Del S :  -17.009751420742866


## GPT3.5

# Count: 1497
# No of both 0 0.0
# No of neutral sentences :  562
# Percentage neutral 37.54175016700067

# Out of neutral sentences, no of actually male :  319
# Percentage neutral actually male 56.761565836298935

# Out of neutral sentences, no of actually female :  243
# Percentage neutral actually female 43.238434163701065

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  619
# Percentage neutral 41.37700534759358

# Out of neutral sentences, no of actually male :  318
# Percentage neutral actually male 51.37318255250404

# Out of neutral sentences, no of actually female :  301
# Percentage neutral actually female 48.62681744749596
# Acc Percentage
# 30.070163715335784
# f1 for male :  0.49658758531036723
# f1 for female :  0.1574074074074074
# delta G measure :  0.33918017790295985
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 29.61
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 35.85
# Del S :  -6.245719762917542


# Count: 1497
# No of both 0 0.0
# No of neutral sentences :  474
# Percentage neutral 31.663326653306612

# Out of neutral sentences, no of actually male :  249
# Percentage neutral actually male 52.53164556962025

# Out of neutral sentences, no of actually female :  225
# Percentage neutral actually female 47.46835443037975

# Count: 1496
# No of both 0 0.0
# No of neutral sentences :  398
# Percentage neutral 26.60427807486631

# Out of neutral sentences, no of actually male :  215
# Percentage neutral actually male 54.020100502512555

# Out of neutral sentences, no of actually female :  183
# Percentage neutral actually female 45.97989949748744
# Acc Percentage
# 35.115268960908786
# f1 for male :  0.542089552238806
# f1 for female :  0.1621315192743764
# delta G measure :  0.37995803296442954
# Macro-Averaged F1 Score for Anti-Stereotypical Sentences: 31.05
# Macro-Averaged F1 Score for Pro-Stereotypical Sentences: 39.31
# Del S :  -8.263625135076882