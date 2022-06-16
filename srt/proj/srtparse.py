from time import sleep
import shlex, subprocess
import threading, os

av_name=""
file_path=<file_path in quotes>
file_video=""
file_srt=""
d={}

def parse_func(s):
    print(os.environ)
    l = [ x.strip() for x in open(file_srt).readlines() ]
    i=0
    j=0
    len_l=len(l)
    while(i<len(l)):
        j=i+l[i:].index('')
        #sleep(2)
        d[l[i+1]]=l[i+2:j]
        i=j+1
        #print(i,j)
    """res={}
    for k in d:
        if s in ' '.join(d[k]):
            res[k]=d[k]
            #print(k,d[k])"""
    return d
import pdb
class popen_thread(threading.Thread):
    def run(self):
        #pdb.set_trace()
        command_line=f"ccextractor {file_video} -o {file_srt}"
        args = shlex.split(command_line)
        proc = subprocess.Popen(args, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_byte, stderr_byte = proc.communicate()
        rc = proc.returncode
        if not rc:
            print(f"return code ={rc}")
            exit()
def run_parse(avname,search_text):
    global av_name,file_video,file_srt
    av_name=avname
    file_video=f"{file_path+av_name}"
    file_srt=f"{file_path+av_name.split('/')[-1].split('.')[0]}.srt"
    t = popen_thread()
    t.start()
    t.join()
    return parse_func(search_text)

