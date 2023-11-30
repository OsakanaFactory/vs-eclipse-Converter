# terminalから自作コマンドを実行したときの処理
# コマンドで指定されたJavaプロジェクトのパスを取得し、そのPathがEclipseで作成されたJavaプロジェクトであれば、
# そのJavaプロジェクトにvscode用のJavaプロジェクトに必要なファイルを追加する

import sys
import os
import shutil
import subprocess
import json
import test

def check_eclipse_project(project_path):
    # 指定されたプロジェクトパスがEclipseで作成されたプロジェクトかどうかをチェックする
    if os.path.exists(project_path + "/.classpath") and os.path.exists(project_path + "/.project"):
        print("\"" + project_path + "\"はEclipseで作成されたプロジェクトです。\n処理を開始します。")
        return True
    else:
        print("\"" + project_path + "\"はEclipseで作成されたプロジェクトではありません。")
        return False

def command():
    # コマンドライン引数からプロジェクトパスを取得する
    if len(sys.argv) != 2:
        print("Usage: python main.py [project_path]")
        sys.exit(1)
    project_path = sys.argv[1]
    return project_path

def log(text):
    # ログを出力する
    date = subprocess.check_output("date", shell=True)
    print(date.decode("utf-8") + "::" + text)

def add_vscode_file(project_path):
    # Eclipseプロジェクトに.vscodeフォルダを追加する
    vscode_folder = project_path + "/.vscode"
    if not os.path.exists(vscode_folder):
        os.makedirs(vscode_folder)
        print(vscode_folder + "に.vscodeフォルダを作成しました.")

# コマンドライン引数からプロジェクトパスを取得
project_path = command()

# Eclipseプロジェクトである場合に.vscodeフォルダを追加
if check_eclipse_project(project_path):
    add_vscode_file(project_path)

test.test1()

 

