const numberButtons = document.querySelectorAll("[number]");
const operationButtons = document.querySelectorAll("[operator]");
const equalsButton = document.querySelectorAll("[equals]");
const deleteButton = document.querySelectorAll("[delete]");
const allClearButton = document.querySelectorAll("[allClear]");
const percentButton = document.querySelectorAll("[percent]");
const previousOperandTextElement = document.querySelectorAll("[previousOperand]");
const currentOperandTextElement = document.querySelectorAll("[currentOperand]");
/*const é imutavel*/

class Calculator {
constructor (previousOperandTextElement, currentOperandTextElement) {
    this.previousOperandTextElement = previousOperandTextElement;
    this.clear();

    }
    formaDisplayNumber(number){
        if (number === "") return "";/* === "" faz comparação com valor e tipo*/
        const stringNumber = number.toString();
        const endWithdDot = stringNumber.endWith(.);
        const integerPart = stringNumber.split(".") [0]; /*split corta o valor, com vírgula, e 0 volta ao start (ínicio de tudo) , ex: 12,5, aparece apenas 12*/
        const decimalPart = stringNumber.split(".")[1]; /*mostra a segunda parte, depois da vírgula ex: 12,5  aparece um dígito*/
        const integerDigits = parseFloat (integerPart); /*transforma o texto em decimal*/

        /*let é mutavél*/

        let integerDisplay;

        if (isNaN(integerDigits)) {
          integerdisplay = ""; /*número que aparece lá em cima, no caso, na tela da calculadora*/
        } else { /*se não*/
            integerDisplay = integerDigits.toLocaleString(pt-Br,{maxiumFractionDigits: 0,}) /*vai transformar em padrão brasileiro.*/
    
      }

      if (endWithdDot) {
        return `${integerDisplay}.`; /*uma espécie de contamitar, mas facilitada. Ele já chama a variavél. Seria a mesmo modelo de usar as aspas.*/
    
        }

        if (decimalPart != null){
            return `${integerDisplay}.${decimalPart}`;

        }

        return integerDisplay
    }

        delete(){
            this.currentOperand = this.currentOperand.toString().slice(0, -1);
        }

        calculate(){
            let result;

            const previous = parseFloat(this.previousOperand); /*resultado da calculadora*/

            const current = parseFloat(this.currentOperand);

            if (isNaN(previous) || isNaN(current)) return; /* ||"" quer dizer "ou", um dos boolean*/

            switch (this.operation){ /*testar vários casos*/

                case "+":

                result = previous + current;
                break;

                case "-" /*subtrai o valor atual do valor anterior.*/
                result = previous - current;
                break;
                

            }

        }

}







/*Imagine uma mochila (variavel), onde estará armazenado/guardado alguma coisa dentro. Let = mochila. Variavel guarda um elemento (texto, número, etc.). Quando chamar a variavel, o dado dentro da variavel será chamado.*/
/*Regras de variações de variaveis - estudar*/
/*let e const são próprias do javascript*/
/*variaveis não podem ter o mesmo nome*/
/*diferenciação entre variavel e função. Sinal de menos e ponto*/
