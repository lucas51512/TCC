@echo off
start %SPARK_HOME%\sbin\start-master.cmd
start %SPARK_HOME%\sbin\start-slave.cmd spark://%COMPUTERNAME%:7077
