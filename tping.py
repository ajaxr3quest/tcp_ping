#!/usr/bin/env python3
#encoding: UTF-8
#
# Coded by @ajax_request
#
from scapy.all import *
import sys
import time
from random import randint


def check_input_regex(input_text, input_regex):
    
    master_regex = {
        "port":r'^[0-9]{1,}$',
        "host":r'(^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$)|(^([a-zA-Z0-9]{1,}[\.]{1}){2}[a-zA-Z]{1,5}$)'
    }
    
    input_text= input_text.strip()
    
    if re.search(master_regex[input_regex], input_text) == None:
        return False
    
    return input_text


def get_arguments():
     
    if len(sys.argv) == 3:
        
        host = check_input_regex(sys.argv[1],"host")
        port = check_input_regex(sys.argv[2],"port")
        
        if host != False and port != False:

            return {
                "host":host,
                "port":int(port),
            }
        
    #else
    print("\nInvalid arguments. Syntax: python tping.py <IP/hostname> <TCP port>")
    sys.exit()
         
 

#full TCP scan = 3 way handshake + RST
def tcp_ping(host,port):
      
    #intentem fer un SYN-ACK amb el host
    src_port= randint(1000,65535)
    packet = IP(dst=host)/TCP(dport=port,sport=src_port,flags="S")
    synack = sr1(packet,verbose=0,timeout=2)
    
    #si no torna resposta
    if synack == None:
        return False
    
    else:
        #enviem ACK
        packet = IP(dst=host)/TCP(dport=port,sport=src_port,flags="A",seq=synack.ack,ack=synack.seq+1)
        send(packet,verbose=0)
        
        #enviem RST
        packet = IP(dst=host)/TCP(dport=port,sport=src_port,flags="R",seq=synack.ack,ack=synack.seq+1)
        send(packet,verbose=0)

        return True
    
    


def tenca():
    
    sys.exit()


if __name__ == "__main__":

    try:
        
        #parseja els arguments de consola
        args=get_arguments()
        print("\nDoing tping against "+args["host"]+" through TCP port "+str(args["port"])+".")
        
        while True:
            try:
                resposta= tcp_ping(args["host"],args["port"])
                if resposta == True:
                    print("Received response from "+args["host"]+" through TCP port "+str(args["port"])+".")
                else:
                    print("Response timeout.")

                #spaguetti code I know, but who cares?
                time.sleep(1)
                time.sleep(1)
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("\n")
                tenca()

    except KeyboardInterrupt:
        print("\n")
        tenca()

    except Exception as e:
        print("\n Looks like something went wrong. Maybe try another day ;)")
