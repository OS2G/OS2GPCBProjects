## How does the microcontroller read switch states
The microcontroller is connected to the switch matrix. The microcontroller pulses voltage through the switches.  From what resources I have looked at, there are two ways to do this.
1. Pulse voltages through each column and read this voltage through the rows
2. Pulse voltages through each row and read this voltage through the columns
There does not seem to be any differences between the two so either can work for our purposes. With how this matrix works, diodes are required after each switch to prevent ghosting (keys that are not pressed are incorrectly read as pressed because of current flowing backwards).
## Types of Switches
### Metal Contact
Metal contact switches are the most common switch type and work by pressing two pieces of metal together to let current travel through them.
#### Positive Action
Positive action switches work by pushing the contacts together to form a connection. The power of the keypress dictates how fast the connection is formed.
![[Positive_action.gif]]
#### Negative Action
Negative action switches work by keeping the contacts separate when the key is not pressed granting one or both of the contacts great potential energy. When pressed, the separation mechanism is released causing the contacts to use this potential energy to make contact and form a connection.

This happens to be the action Cherry MX switches use.
![[Negative_action.gif]]
### Membrane
Membrane switches work similar to metal contact switches except that they use exposed electrical traces in place of the pieces of metal. These traces are either bridged together using a conductive object or by flexing a membrane against another membrane.
### Reed
Reed switches are similar to metal contact switches in that there are pieces of metal that connect to form a current. This difference is that the force the brings them together is magnetic rather than physical.
## Resources
- https://www.masterzen.fr/2020/05/03/designing-a-keyboard-part-1/
- https://deskthority.net/wiki/Main_Page
