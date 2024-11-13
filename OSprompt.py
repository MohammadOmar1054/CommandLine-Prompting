import os
import random 
fi_le = 44

# from pip import ask_inst_app , execution 

LIST_OF_CommandCodes = ' CommandCodes : \n Turn-Off-OS[1] \n Close-App[2] \n Start-App[3] \n Hack-kWifi-Password[4] \n InstallPackages[5]'
print(LIST_OF_CommandCodes)
def execute(x): 
    print('okay')
while True:                   # WHIlE LOOP CONDITIONED TRUE TO REPEAT FOREVER
    print('.............')

    # This programm only accomplishess 3 tasks
    ask_main = int(
        input('Enter a CommandCode for execution or Enter "0" to display CommandCodes :'))
    if ask_main == 0:
        print(LIST_OF_CommandCodes)
    elif ask_main == 1:
        try:
            # shutdown or restart
            ask_power = str(
                input('Enter S to shutdown or R to restart your Computer :'))
            try:
                if ask_power == 's' or ask_power == "S":
                    final_dec = str(
                        input('Do you really want to shutdown your PC ? y or n :'))
                    if final_dec == 'y' or final_dec == 'Y':
                        print('Command Comprehension Completed...')
                        print('Shutting down PC......')
                        os.system('shutdown /s /t 5')  # SHUTDOWN PROGRAM
                    elif final_dec == "n" or final_dec == 'N':
                        print('Why are you afraid ? ')

                    if ask_power == 'r' or ask_power == "R":
                        final_dec_res = str(
                            input('Do you really want to Restart your PC y or n : '))
                    if final_dec_res == 'y' or final_dec == 'Y':
                        print('Command Comprehension Completed...')
                        print('Restarting PC......')
                        os.system('shutdown /r /t 5')  # RESTART PROGRAM
                    elif final_dec_res == "n" or final_dec == 'N':
                        print('Why are you so scared ? ')
                    else:
                        print('Please come prepared....')

            except:
                print('Pleasse come prepared...') 
        except:
            print('Input Recieved Contained Typo')
    elif ask_main == 2:
        ASK_TASK_TO_END = str(
            input('Enter the name of the Task/App that you want to End/Close :'))
        # TASK KILL PROGRAM
        os.system('taskkill /im {}.exe'.format(ASK_TASK_TO_END))


    elif ask_main == 3:
        ASK_APP_TO_START = str(
            input('Enter the name of the App you want to start : '))
        print("Launching", ASK_APP_TO_START + ".....")
        os.system('START {}.exe'.format(ASK_APP_TO_START))

    # else:
    #     print('Please come prepared.....')
    elif ask_main == 4:
        SERVE_ALL = print('Enter Null to review password history! ')
        ASK_WIFI_NAME = input('Enter the name of your network... : ')
        print(os.system('netsh wlan show profile {} key = clear'.format(ASK_WIFI_NAME)))


    elif ask_main ==5:
        ASK_PACKAGE = input('Enter the name of the package : ')                        


                                                                                                                                                                                                                                                                                                                                                                                                                                         
        os.system('pip install {}'.format(ASK_PACKAGE))
        if ASK_PACKAGE in ['numj , NUMJ,numJ,NumJ']: 
            for i in range(123):
                print('NUMJ IS THE BEST')
            else:
                execute(fi_le)