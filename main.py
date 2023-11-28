# terminalから自作コマンドを実行したときの処理
# コマンドで指定されたJavaプロジェクトのパスを取得し、そのPathがEclipseで作成されたJavaプロジェクトであれば、
# そのJavaプロジェクトにvscode用のJavaプロジェクトに必要なファイルを追加する

import sys
import os
import shutil
import subprocess
import json
import sys
import os

def check_eclipse_project(project_path):
    # eclipseで作成されたJavaプロジェクトかどうかチェックする関数
    # .classpathと.projectファイルが存在するかチェック
    if os.path.exists(project_path + "/.classpath") and os.path.exists(project_path + "/.project"):
        # exlipseで作成されたプロジェクトの場合
        log("\"" + project_path + "\"はEclipseで作成されたプロジェクトです。処理を開始します。")
        return True
    else:
        log ("\"" + project_path + "\"はEclipseで作成されたプロジェクトではありません。")
        return False


# コマンドの設定をする関数
def command():
    # project_pathをグローバル変数として扱う
    global project_path
    # python main.py [project_path]で実行されたときの処理
    project_path = sys.argv[1]
    return project_path

def log(text):
    # ログに日時を追加して出力する関数
    date = subprocess.check_output("date", shell=True)
    print(date.decode("utf-8") + "::" + text)

# vscode用のJavaプロジェクトに必要なファイルを追加する関数
def add_vscode_file():
    # project_pathに.vscodeフォルダが存在しない場合のみ作成
    vscode_folder = project_path + "/.vscode"
    if not os.path.exists(vscode_folder):
        os.makedirs(vscode_folder)
        log(vscode_folder + "に.vscodeフォルダを作成しました。")
    

check_eclipse_project(command())



 

