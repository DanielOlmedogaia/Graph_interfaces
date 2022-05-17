# La clase QCheckBox

Los checkBoxes son objetos de la clase QCheckBox a diferencia de los objetos
de la clase QRatioButton, que son mutuamente excluyentes, dos o mas checkBoxes 
pueden estar activos a la vez, o bien, inactivos.
## Metodos de la clase QCheckBox
alguno de los metodos para esta clase son
\
- <span style="color:red">isChecked()</span> : Este metodo devuelve un valor boleano verdadero si el checkBox está marcado y falso en otro caso.
- <span style="color:red">SetTristate()</span>
 : Se usa cuando no quiere que el estado de la casilla cambie, se mantiene seleccionado cuando el valor boleano es verdadero y deseleccionado cuando el valor boleano es falso.

- <span style="color:red">setIcon()</span> :
Para insertar un icono
- <span style="color:red">SetText</span>: 
Para insertar texto 
- <span style="color:red">SetChecked</span>:
Si se le pasa un valor boleano verdadero, la casilla estará seleccionada por default, no confunda con setTristate ya que este último no permite cambiar el estado de la casilla.
## Señales de la clase QcheckBox
- <span style="color:green">Clicked()</span> : 
Esta señal se emite cuando la casilla ha sido activada
- <span style="color:green">stateChanged()</span> :
Se emite cuando la casilla ha cambiado de estado (de checked a unchecked y viseversa)
