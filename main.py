# terminalから自作コマンドを実行したときの処理
# コマンドで指定されたJavaプロジェクトのパスを取得し、そのPathがEclipseで作成されたJavaプロジェクトであれば、
# そのJavaプロジェクトにvscode用のJavaプロジェクトに必要なファイルを追加する

import sys
import os
import shutil
import subprocess
import json

def check_eclipse_project(project_path):
    # .classpathと.projectファイルが存在するかチェック
    if os.path.exists(project_path + "/.classpath") and os.path.exists(project_path + "/.project"):
        # exlipseで作成されたプロジェクトの場合
        print("\"" + project_path + "\"はEclipseで作成されたプロジェクトです。処理を開始します。")
        return True
    else:
        print ("\"" + project_path + "\"はEclipseで作成されたプロジェクトではありません。")
        return False
        
    

# コマンドの設定をする関数
def command():
    project_path = sys.argv[1]
    return project_path


check_eclipse_project(command())


