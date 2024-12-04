import subprocess

def calculate_entropic_relevance(log_name, dfg_name):
    try:
        args = []
        args.append('java')  # Запуск Java
        args.append('-cp')  # Указание classpath
        # Указываем все необходимые JAR-файлы через точку с запятой (для Windows)
        args.append('jbpt-pm-entropia-1.6.jar;commons-cli-1.9.0.jar')
        args.append('org.jbpt.pm.tools.QualityMeasuresCLI')  # Указываем основной класс
        args.append('-r')  # Параметры для основного класса
        args.append('-s')
        args.append('-rel')
        logstring = log_name + '.xes'  # Имя лог-файла
        args.append(logstring)
        predstring = dfg_name + '.json'  # Имя JSON-файла
        args.append('-ret')
        args.append(predstring)

        # Запуск команды и получение результата
        result = subprocess.check_output(args)
        result_s = float(result)  # Преобразуем результат в число
    except Exception as e:
        result_s = 'NA'
        print("Error:", e)  # Вывод ошибки, если она возникла

    return result_s

