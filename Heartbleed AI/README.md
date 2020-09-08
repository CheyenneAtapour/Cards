# Cards

This program simulates a 1k HP opponent which summons increasingly more powerful monsters at a cap of 50/50

The idea is to play your cards physically in front of the AI opponent, and keep track of your own cards and effects. Apply damage to AI accordingly. You can assume the AI attacks the most important monsters you control, or just random monsters you control. 

Option 1:
You will be prompted to select a target.
You select targets by inputting numbers and then enter
0 is the first monster, 1 is the second monster, 2 is the third monster, and so on
-1 is the opponent (direct hero attack)
once you have typed in the target and pressed enter, you will be prompted on how much damage you are doing to the specified target.
You must type the damage amount and hit enter
The battlefield will refresh and show the updated state once this damage has been applied.

Option 2:
You will be prompted to enter a board clear damage amount
You must type in an integer value and hit enter on your keyboard
Once you have done this, the battlefield state will be updated after applying the specified damage to all the monsters on the battlefield.

Option 0:
This will update the battlefield and show the main menu again.
The AI is programmed to summon monsters every other turn, starting with a 10/10, and moving up to 50/50, where it will summon these monsters every other turn.


Please suggest added features to improve testing.