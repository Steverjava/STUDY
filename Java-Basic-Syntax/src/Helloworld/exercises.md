### 一、填空题

1. Java 划分为三个技术平台，分别是________、Java EE 和 Java ME。

——*Java SE* 
2. Java 的特点有简单、________、安全性、跨平台性、支持多线程、分布性。

——*面对对象*
3. Java 中提供了________命令用于执行字节码文件。

——*java(`java [options] <classname> [args]`)*
4. Java 程序运行时，必须经过________和运行两个步骤。

——*编译*
5. JRE 是 Java 程序的________环境。

——*运行时*

### 二、判断题

1. JRE 中包含了 Java 基本类库、JVM 和开发工具。（ *✘*）——JDK
2. 编译 Java 程序需要使用 java 命令。（ *✘*）——javac
3. IDEA 开发工具 Debug 模式下不进入函数内部的单步调试快捷键是 F7。（ *✘*）
——F8（步过）、F7（步入）
4. JDK 8 以后可以不用配置 classpath 环境变量。（ *✔*）
5. Java 是一种面向过程的语言。（ *✘*）——面向对象

### 三、选择题

1. 下列选项中，对于 Java 语言的类别描述正确的是（*C*）。
   A、机器语言
   B、汇编语言
   C、高级语言
   D、以上都不对
2. 下列选项中，属于 Java 的特点的有（*ABCD*）。（多选）
   A、简单性
   B、面向对象
   C、跨平台性
   D、支持多线程
3. 下列选项中，关于 JDK 中 java.exe 的作用描述正确的是（*D*）。
   A、Java 文档制作工具
   B、Java 解释器
   C、Java 编译器
   D、Java 启动器
4. 下列选项中，属于 JDK 中包含的工具的有（*ABCD*）。（多选）
   A、Java 编译器
   B、Java 文档生成工具
   C、Java 运行工具
   D、Java 打包工具
5. 下列选项中，为 Java 中字节码文件后缀的是（*D*）。
   A、.java
   B、.jre
   C、.exe
   D、.class

### 四、简答题

1. 简述 Java 的特点。

***Java具有简单、面对对象、安全、可跨平台、支持多线程、分布性等特点***
2. 简述 Java 的运行机制。

***Java程序运行时，需先将Java源文件编译为.class字节码文件，后交由JVM对其进行解释执行，并展示结果。***

### 五、编程题
使用记事本编写一个 Hello World 程序，并在命令提示符窗口编译运行，并打印输出结果。

```java
public class HelloWorld{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```
>\>>> Hello World