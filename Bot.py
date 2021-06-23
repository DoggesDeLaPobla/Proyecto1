from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import cv2

f = open("bot.key", "r")
key=f.read()
f.close()
modo=0


def start(update, context):
    update.message.reply_text("Hola soy BitBot Tu asistente para perros y gatos\nA continuación un pequeño ejemplo de uso\nPrimero indicame tu tipo de mascota Perro o Gato\n /Animal Perro /Animal Gato /Animal Ambos\n En caso de cualquier error o asistiencia escribe /help")

def animal(update, context):
    if len(update.message.text)>len("/Animal") and (str(update.message.text).split(" ")[1]=="Perro" or str(update.message.text).split(" ")[1]=="Gato" or str(update.message.text).split(" ")[1]=="Ambos"):
        f = open("usuarios.codec", "r")
        copy=""
        est=False
        f2=f.readlines()
        for i in f2:
            if i.count(str(update.message.chat.id))>0:
                copy+="Usuario: "+str(update.message.from_user.first_name)+" Clave: "+str(update.message.chat.id)+" Tipo: "+str(update.message.text).split(" ")[1]+"\n"
                est=True
            else:
                if len(i)>5:
                    copy+=i+"\n"
        if not est:
            copy+="Usuario: "+str(update.message.from_user.first_name)+" Clave: "+str(update.message.chat.id)+" Tipo: "+str(update.message.text).split(" ")[1]
        s=""
        for i in copy.split("\n"):
            if len(i)>5:
                s+=i+"\n"
        f.close()
        f=open("usuarios.codec","w+")
        f.write(s)
        f.close()
        update.message.reply_text("Tu tipo de animal a sido anclado a tu perfil!\nEsta es una foto del lugar de donde te notificare")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('frame1.jpg','rb'))
    else:
        update.message.reply_text("No me has especificado correctamente tu tipo de animal\nRecuerda que acepto: /Animal Perro /Animal Gato /Animal Ambos")


def config(update, context):
    global modo
    if modo==0:
        modo=1
        update.message.reply_text("Hola ahora quieres configurar el area de deteccion")


def image_handler(update, context):
    global modo
    if modo==1:

        photo_file = update.message.photo[-1].get_file()
        photo_file.download('./deteccion.jpg')
        
        img = cv2.imread("./deteccion.jpg")
        img = cv2.resize(img, (1280,720))


if __name__ == '__main__':
    
    updater = Updater(key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('animal', animal))
    dispatcher.add_handler(CommandHandler('config', config))
    dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))


    updater.start_polling()