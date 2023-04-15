from PyQt5 import uic,QtWidgets
import mysql.connector

id_value = 0

banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="cadastro_pet"
)

def funcao_principal(): 
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    tipo = ""
    
    if formulario.radioButton.isChecked() :
        tipo = "Cachorro"
    else:
        tipo = "Gato"
        
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pets (nome,idade,raca,tipo) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),tipo)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


#def excluir():
 
#def editar_dados():
   
     
def salvar_dados():
    global id_value
    nome = tela_editar.lineEdit_2.text()
    idade = tela_editar.lineEdit_3.text()
    raca = tela_editar.lineEdit_4.text()
    tipo = tela_editar.lineEdit_5.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE pets SET nome = '{}', idade = '{}', raca = '{}', tipo = '{}' WHERE id = {}".format(nome,idade,raca,tipo,id_value))
    
    tela_editar.close()
    segunda_tela.close()
    pegar_tela()
    
def pegar_tela():
    segunda_tela.show()
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pets"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
      
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)
    
    for i in range(0, len (dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    
    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_pets.ui")
tela_editar=uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(pegar_tela)
tela_editar.pushButton.clicked.connect(salvar_dados)


formulario.show()
app.exec()


