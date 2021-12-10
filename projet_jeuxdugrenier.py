import csv



def fn_question(question):
    return input(question)



def fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, platforme, note) :
    file_csv = "projet_jeuxdugrenier.csv"
    with open(file_csv,"w",encoding="utf-8",newline="") as fichier:
        header = ["nom_du_jeu", "editeur", "genre", "annee_de_sortie", "platforme", "note"]
        data = [nom_du_jeu, editeur, genre, annee_de_sortie, platforme, note]
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


def fn_oldschool(annee_de_sortie):
    if(annee_de_sortie) <= 2006:
        return True
    else:
        return False


q_nom_du_jeu = "entrez le nom du jeu :"
nom_du_jeu = fn_question(q_nom_du_jeu)
q_editeur = "entrez editeur :"
editeur = fn_question(q_editeur)
q_genre = "entrez le genre :"
genre = fn_question(q_genre)
q_annee_de_sortie = "entrez annee de sortie :"
annee_de_sortie = int(fn_question(q_annee_de_sortie))
q_platforme = "entrez le platforme :"
platforme = fn_question(q_platforme)
q_note = "entrez la note :"
note = fn_question(q_note)

fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, platforme, note)

if fn_oldschool(annee_de_sortie):
    print("le jeu est sorti avant")
else:
    print("le jeu est sorti après")

