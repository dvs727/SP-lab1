#!/bin/bash

echo 'Автор: Дубоносов Вячеслав'

answer="y"
username="root"

while [ "$answer" != "n" ]
do
  #•	запрашивает имя пользователя
  echo "gimme username"
  read username

  if grep $user /etc/passwd
  then
    #o	если указанный пользователь не зарегистрирован в системе, то выводит сообщение об этом и повторно запрашивает имя пользователя
    echo "Ошибка пользователя нет"
    continue
  fi

  #•	если указанный пользователь зарегистрирован в системе, то выводит его уникальный идентификатор (UID)
  id $username -u

  #и имена групп, в которые входит этот пользователь, разделенные пробелом
  groups $username

  #o	основная (первичная) группа должна быть указана отдельно
  id $username -g -n

  echo 'Continue? y/n'
  read answer

  while [ "$answer" != "y" ] && [ "$answer" != "n" ]
  do
  	echo 'Continue? y/n'
	read answer
  done

done


