#!/bin/bash

codigo="Blackboard Game.cpp"
executavel="a.out"

casos=1

for i in $(seq 1 $casos); do
   echo "Caso $i"
   g++ "$codigo" -o "$executavel" || exit 1 # compila o código e sai se houver erro
   ./"$executavel" < "in$i.txt" > "myout$i.txt"
   diff "myout$i.txt" "out$i.txt"

   if [ $? -eq 0 ]; then
       echo "✅ Caso $i passou"
   else
       echo "❌ Caso $i falhou"
       echo "Esperado:"
       cat "out$i.txt"
       echo "Obtido:"
       cat "myout$i.txt"
   fi
   echo "----------------------"

done
