#!/usr/bin/env python
# -*- coding: utf-8 -*-
from capturador_armas import adicionar_arma
from treinador_armas import treinar_reconhecimento_armas 
from reconhecedor_armas import reconhecer_armas
import pickle
import os

guns = []

def mostrar_menu():
    
	print ("(1) Adicionar face")
	print ("(2) Reconhecer faces")
	print ("(0) Sair")
	print ("\n")
	resposta = int(input("Resposta: "))
	
	return resposta
	
def adicionar_arma():
	nome = input("Modelo: ")
	guns.append(nome)
	numero_armas = len(guns)
	adicionar_gun(numero_armas)
	salvar_arma()
    #print ("\n [INFO] Treinando reconhecimento, aguarde...")
	treinar_reconhecimento_armas()

def salvar_arma():
	with open("guns.data", "wb") as arquivo_guns:
		pickle.dump(guns, arquivo_guns)

def carregar_armas():
	if (os.path.isfile("guns.data")):
		with open("guns.data", "rb") as arquivo_guns:
			return pickle.load(arquivo_guns)
	
	return []

def main():
	guns = carregar_armas()
	while(True):
		opcao = mostrar_menu()
		if(opcao == 1):
			adicionar_arma()
		elif (opcao == 2):
			reconhecer_armas(guns)
		elif(opcao == 0):
			break

if __name__ == "__main__":
	main()