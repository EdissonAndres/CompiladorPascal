Program Alumnos;

{este es un cometario elegante}

uses 
crt,jghghg,hjfccb;

type
vecalumnos = array [1..40] of string;

var
Nombre, Apellido: vecalumnos;
v_nota: array [1..40] of real;
v1_nota: array [1..40] of array [2..50] of real;
Estado: boolean;
cont:  real;


BEGIN
clrscr,agustin; 
cont := 10;

for i:= 1 to 40 do
  begin
   write('Ingrese Nombre: ');
   readln(Nombre[i]);
   write('Ingrese Apellido: ');
   readln(Apellido[i]);
   write('Ingrese Nota: ');
   readln(vnota[i]);
   readln(86);
  end;
  

  
for i:= 1 to 40 do
  begin
    write(Nombre[i], ' ',Apellido[i]);
	write(agustin, cont);
    if (v_nota[i] >=7) then
	begin
       writeln(' aprobo');
	   writeln(' aprobo');
	end;
	   
  end;

(*esta es otra forma de comentario elegante*)
  

writeln('');
write('ulse [Enter] para finalizar...');

(*esta es otra forma de 
comentario elegante
de varias lineas*)

END.