__author__ = 'tmaslon@hidglobal.com'


import argparse
import os

# source root of application usually go back two folders up
source_root = "..\\.."

#Java Development Kit folder
jdk_path = os.getenv('JAVA_HOME')

#Android sdk folder
android_env_list = ['ANDROID_HOME', 'ANDROID_SDK', 'ANDROID_SDK_HOME']
for _android_sdk_path_name in android_env_list:
    android_sdk_path = os.getenv(_android_sdk_path_name)
    if android_sdk_path != None:
        break
if android_sdk_path == None:
    print "Please define any of these environment variable", android_env_list[0:len(android_env_list)]," pointing to your Android SDK"
    exit()



parser = argparse.ArgumentParser(description='Builds xchip android projects')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')


args = parser.parse_args()
print args.accumulate(args.integers)

