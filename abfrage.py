# -*- coding: utf-8 -*-
import random

# ----------------- Software Engineering Klausurvorbereitung -----------------
'''
question_number = int()
correct = int()
false = int()
'''
l_o_q = []
l_o_cat = []

# Allgemeine Fragen und Konzepte
high_performance_computing = [
    ("HPC Merkmale", "parallelisierbar, schnelle Prozessoren, Bandbreite, geringe Latenz"),
    ("HTC Merkmale", "viele, gleiche unabhängige parallelisierbare Anwendungen, viele Prozessoren, I/O Bandbreite"),
    ("Seq. Merkmale", "sehr leistungsstarke Prozessorenm, ggf I/O Bandbreite"),
    ("Bandbreite", "daten die pro Zeiteinheit transferiert werden/können"),
    ("Latenz in HPC", "Zeit zwischen dem erstmaligen Anfragen der Daten und der Ankunft des ersten Bytes"),
    ("Latenz in HPC Zeiteinheit", "nano Sekunden"),
    ("Transfer Time", "Latenz + Menge der Daten / Bandbreite"),
]
# Flynn's Taxonomie
flynny_taxonomie = [
    ("SISD", "system mit einem prozessor führt eine Operation nach der anderen aus."),
    ("SIMD", "system mit mehreren prozessoren die die selbe operation auf verschiedenen Daten ausführen"),
    ("MISD", "system mit mehreren prozessoren die unterschiedliche Operationen auf dem selben DatenObjekt ausführen"),
    ("MIMD", "system mit mehreren prozessoren die unterschiedliche Operationen auf verschiedenen Daten ausführen"),

    ("SISD tradeoffs", "keine Parallelisierbarkeit, geringe Kosten geringe Komplexität, "
                       "geschwindigkeit des Einen Prozessors limitierender Faktor"),
    ("SIMD tradeoffs", "erlaubt für Parallelisierbarkeit, ist jedoch in der Menge der Befehle limitiert, "
                       "da alle prozessoren die selbe instruktion ausführen müssen"),
    ("MISD tradeoffs", "erlaubt für Parallelisierbarkeit, Prozessoren müssen sich jedoch koordinieren, "
                       "was zu komplexen systemdesigns führt"),
    ("MIMD tradeoffs", "erlaubt für Befehls- und Daten-Parallelisierbarkeit was mehr Flexibilität und "
                       "performance bringen kann, verlangt jedoch ebenso eine Koordination zwischen "
                       "Prozessoren"),
]
# von Neumann Bottleneck und was dagegen getan wird
von_neumann_bottleneck = [
    ("von Neumann Bottleneck", "prozessoren können schneller Daten verarbeiten, als dass sie mit neuen Daten aus "
                               "dem hauptspeicher befüttert werden können"),
    # TODO memory hierarchy, pipelining
    ("Neumann BN Lösungsansätze", "caching, pipelining, memory hierarchy"),
    ("Speicher Hierarchie ", "register -> L1 L2 L3 -> main memory"),
    # muss natürlich nich so sein, fürs Verständniss der Größenordnung
    ("Caches auf jedem core", "L1 32kB & L2 256kB"),
    ("Caches auf mehreren cores", "L3 2MB/core"),
    ("Verzögerung L1 L2 L3", "5 15 30 Zyklen"),
    ("Größe von Cache Lines", "64 oder 128 B/line"),
    ("Cache datenstruktur", "Kopie von fortlaufenden RAM-Daten"),
    ("Instruction Pipelining", "Bestandteile von mehreren Operationen werden parallel durchgeführt, d.h. während "
                               "(selber Zyklus) z.B. eine Zahl addiert wird, wird die nächste Op. "
                               "bereits aus dem Speicher geladen"),
]
memory_distribution = [
    ("Shared Memory Systeme Merkmale", "Mehrere Kerne sitzen auf der selben Speicheranbindung (z.B. bus) "
                                       "und teilen sich den Hauptspeicher (teilen Adressraum)"),
    ("Shared Memory Syteme Vorteile" , "globaler Adressraum, leicht zu programmieren"),
    ("Shared Memory Syteme Nachteile", "Skalierung"),
    ("Shared Memory Syteme Programmiermodelle", "OPENMP, Pthreads, auch MPI, CILK"),

    ("Distributed Memory Syteme Merkmale", "jeder Processor hat seinen eigenen Speicher (also Adressraum) "
                                           "entscheidend für dei Performance ist die Netzwerktopologie"),
    ("Distributed Memory Syteme Vorteile", "Skalierbarkeit durch hinzufügen von Knoten"),
    ("Distributed Memory Syteme Nachteile", "schwieriger zu programmieren, overhead durch Interprozesskommunikation"),
    ("Distributed Memory Syteme Programmiermodelle", "send-receive über Message Passing Interface, MPI, OpenMPI, PVM"),
    ("DMS Surface-To-Volume Ratio Merkmale", "Verhältnis von benötigter Kommunikation zwischen den Knoten "
                                             "und deren Prozessorleistung"),
    ("DMS gutes Surface-To_Volume Ratio", "ein tiefes Verhältnis heist es ist wenig Kommunikation für viel "
                                          "Rechenleistung nötig. Das Programm läuft effizient und ist gut skalierbar"),
    ("DMS schlechtes Surface-To_Volume Ratio", "ein hohes Verhältnis heist es findet viel Kommunikation "
                                               "(viele Daten, oder häufige Messages oder großer Komm-Overhead) "
                                               "statt, die Rechenleistung ist jedoch recht gering."),

    ("Distributed Shared Memory Syteme Merkmale", "Jede CPU hat einen eigenen lokalen Speicher, "
                                                  "ansprechbar auch von anderen CPUs "
                                                  "Speicherzugriffszeiten unterscheiden sich (NUMA), "
                                                  "gemeinsamer Adressraum"),
    ("Distributed Shared Memory Syteme Vorteile", "schneller memory access falls lokal vorhanden, trotzdem"
                                                  "hierarchische speicher Organisation (gem. Adressraum), "
                                                  "hohe Speicher Bandweite"),
    ("Distributed Shared Memory Syteme Nachteile","Vorteile kommen erst wirklich zur Geltung wenn Programm "
                                                  "den Speicher effizient Organisiert "
                                                  "und die variierende Latenz berücksichtigt"),
    ("Distributed Shared Memory Syteme Programmiermodelle", "MPI, OpenMP, spezielle APIs und alloc routinen"
                                                            " von hardware Herstellern"),

    ("loosely coupled systems", "mehrere Prozessoren mit eigenem Speicher sind anstatt über Hochgeschwindigkeit-"
                                "Verbindungen (e.g. Infiniband) übers internet Verbunden"),

]

memory_access = [
    ("UMA", "uniform memory access"),
    ("UMA Merkmale", "Zugriffszeiten auf jeden Bereich des Speichers sind gleich"),
    ("UMA varianten", "ohne Cache, mit Cache, mit privatem Speicher (für den Programmcode)"),
    ("UMA Limitierung", "Multiprozessoren mit deutlich mehr als 100 CPUs sind "
                        "UMA- Architekturen nicht geeignet (zu viel Hardware nötig)"),
    ("UMA nicht blockierendes Netzwerk Beispiel", "Kreuzschienenverteiler (crossbar switch)"),
    ("UMA blockierendes Netzwerk Beispiel", "Omega Netzwerk (braucht deutlich weniger switches)"),

    ("NUMA", "nonuniform memory access"),
    ("NUMA Merkmale", ""),
    ("NUMA ", "Zugriffszeiten auf den Speichers können unterschiedlich sein"),
]

network_architectures = [
    ("eindimensionale Netzwerkstrukturen", "Lineares Array, Ring"),
    ("zweidimensionale Netzwerkstrukturen", "Mesh Netzwerk, 2DTorus"),
    ("mehrdimensionale Netzwerkstrukturen", "3+D-Torus, Hypercubes"),
    ("Fat Tree Merkmale", "mehrere Ebenen mit Switchen, Switche haben gleich viele Verbindungen "
                          "nach oben und nach unten, Anzahl der Links steigt mit jeder Ebene"),
    ("Fat Tree Latenz", "größer, je weiter die Nodes voneinander entfernt sind"),
    ("fully-non-blocking Merkmale", "Keine Kollisionen da jede Prozessoreinheit direkt mit jeder anderen verbunden ist"),
    ("fully-non-blocking Netzwerke Beispiele", "torus, fat-tree"),
]
l_o_q.append(high_performance_computing)
l_o_cat.append("high performance computing")
l_o_q.append(flynny_taxonomie)
l_o_cat.append("flynny taxonomie")
l_o_q.append(von_neumann_bottleneck)
l_o_cat.append("von neumann bottleneck")
l_o_q.append(memory_distribution)
l_o_cat.append("memory distribution")
l_o_q.append(memory_access)
l_o_cat.append("memory access")
l_o_q.append(network_architectures)
l_o_cat.append("network architectures")


def ask_random_question(question_number, question, category):
    print("\n")
    print("-------------------------")
    print(str(question_number + 1) + ")")
    print("Question from the " + l_o_cat[category] + " category.")
    print(question[0])

    answer = input()
    if answer == question[1]:
        print("!!! Richtig !!! ")
        return question[0], answer, 1
    # Antwort stimmt nicht 1 zu 1 überein
    else:
        print("The answer was:  " + question[1])
        if len(answer) != 0:
            print("Was the your answer actually correct? Then type 1, y or yes.")
            overrule = input()
            if len(overrule) == 0:
                return question[0], answer, 0
            elif overrule == 'y' or overrule == 'yes':
                return question[0], answer, 1
            elif int(overrule) == 1:
                return question[0], answer, 1
        else:
            return question[0], answer, 0


def get_rand_question(questions_done):
    # chooses a random category
    category = random.randint(0, len(l_o_q) - 1)
    # chooses a question from that cat
    n_question = random.randint(0,len(l_o_q[category]) - 1)

    while [category, n_question] in questions_done:
        category = random.randint(0, len(l_o_q) - 1)
        n_question = random.randint(0, len(l_o_q[category]) - 1)

    questions_done.append([category, n_question])
    return l_o_q[category][n_question], category, n_question


def new_round(number_of_questions):
    answers = list()
    questions_done = list()
    question_number = 0
    num_correct_answers = 0
    num_false_answers = 0

    for i in range(number_of_questions):
        (question, category, n_question) = get_rand_question(questions_done)
        answers.append((n_question, ask_random_question(question_number, question, category), category))
        question_number += 1

    print("\n")
    print("-------------- Auswertung --------------")
    print("\n")

    print("0 = Info ")
    print("1 = Wiederholung der falschen geht noch nich")
    choice = input()
    if int(choice) == 0:
        auswertung_info(answers, num_correct_answers, num_false_answers)
    else:
        auswertung_info(answers, num_correct_answers, num_false_answers)
        # auswertung_wiederholung(answers, num_correct_answers, num_false_answers)


def auswertung_info(answers, correct, false):
    for answer in answers:
        if answer[1][2] == 1:
            correct += 1
        else:
            print("\n")
            print("-------------------------")
            print("Frage: " + str(answer[1][0]) + " war Falsch:")
            print(answer[1][1])
            print("Richtige Antwort: ")
            print(l_o_q[answer[2]][answer[0]][1])
            false += 1

    print("\n")
    print("Stats")
    print("Correct: " + str(correct))
    print("False: " + str(false))
    print("\n")

    if false == 0:
        print("---------------------------------------------------------")
        print("------------- !!! ALLLE FRAGEN RICHTIG !!! --------------")
        print("---------------------------------------------------------")

'''
def auswertung_wiederholung(answers, correct, false):
    for answer in answers:
        if answer[2] == 1:
            correct += 1
        else:
            print("\n")
            print("-------------------------")
            print("Frage: " + str(answer[1][0]) + " war Falsch:")
            print(answer[1][1])
            print("Richtige Antwort: ")
            print(l_o_q[answer[2]][answer[0]][1])
            false += 1
            while True:
                z = input()
                if str(z) == l_o_q[answer[0]][1]:
                    print("True")
                    print("\n")
                    false -= 1
                    break
                else:
                    print("False. repeat!")
                    print("\n")
            false += 1

    print("Stats")
    print("Correct: " + str(correct))
    print("False: " + str(false))
    print("\n")

    if false == 0:
        print("---------------------------------------------------------")
        print("------------- !!! ALLLE FRAGEN RICHTIG !!! --------------")
        print("---------------------------------------------------------")
'''

# ---------------- MAIN ----------------

def init():
    print("\n")
    print("---------------------------------------------------------")
    print("--------------- !!! ABFRAGEPROGRAMM !!! -----------------")
    print("---------------------------------------------------------")

    print("Wie fiele Fragen sollen abgefragt werden?")
    q = int(input())
    print("------------------------- START --------------------------")
    return q


while True:
    new_round(init())

    print("1 = repeat 0 = exit")
    r = int(input())
    if r == 1:
        pass
    else:
        break
