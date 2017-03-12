#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
import web
import thread
from itchat.content import TEXT

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.message_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

def t_send(msg,toUserName='filehelper'):
    try:
        itchat.send_msg(msg=msg,toUserName=toUserName)
        return
    except (ConnectionError,NotImplementedError,KeyError):
        traceback.print_exc()
        print('\nConection error,failed to send the message!\n')
        return
    else:
        return
# Start auto-replying
@itchat.msg_register(TEXT)
def simple_reply(msg):
    itchat.send("Now reply", toUserName='filehelper')
    print 'I received: %s' % msg['Content']
    text = u'你刚才说: %s' % msg['Content']
    t_send(text, msg['FromUserName'])


if __name__ == "__main__":
  itchat.auto_login(enableCmdQR=2,hotReload=True)
  t_send(u"开始干活", toUserName='filehelper')
  thread.start_new_thread(itchat.run, ())

  app.run()
