U
  �Q;` �           �  d dl Z d dlZd dlZzd dlZd dlZW n(@ek
rTe�d�e�d�Y nX d dlmZd dlmZm	Z	m
Z
e
ZeZejZejZejZejZejZe� d�Ze� d�Zdd	� Ze�d
�dZe� dd� Ze� dS )�  zpip install googlesearchzpip install colorama)�search)�Fore�Back�Stylez!|                               |z!=================================c          C  s0 �&��'�7�G���dzr   
|                               |
|===============================|
|-------------------------------|
~~~+]zBy: Anikin Lukez[+]~~~
            ZdORKERz�       

|-------------------------------|
|===============================|
|                               |
|                               |)�Wrint�y�ZBRIGHT�r�� r   �dork.py�fanner 
   �
�r �Vlear� c            : z�t t� dt� dt� d��} t t� dt� dt� d��}t t� dt� dt� d��� tt�tt�� fdd�}d}d}t| d	d
t|�dd dd�D ]P}|d }tt� |�t	�
d�|d7 }|t|�kr�q�|}||�t	�
d�q�W n@tk
�rtdt� d��t	�
d�t�d�Y nX tdt� d��t�� d S )N�z  [!]Enter a Dork:� z  [!]Enter Amount Value:z  [!]Output file name:c       @   s2 ��'�'������ Dz.txt�a�)�open�write�7tr�close)�Gser�File��6ogr   �logger0  s  dorks.locals>loggerr 6omZen� e7ldZlangZnum�Wtart�stop�pause� g�������?r  z![x] User Interruption Detected.!g   �?u ✅️] Complete!!)�inputrp �gr` �line�line2r  �intr
  �time�sleep�KeyboardInterruptr	 �7ys�exit)ZdorkZamountr Gequ�FlagZwesultsr   r   �dorks) 2    @@
@@
r- r'  �osr* googlesearchZcolorama�ImportError�systemr 0 r P r �ZREDr	  ZGREENr#  ZYELLOWr DLUE�ZCYANr
 $  r%   r -  r   r   �<module> s.     0'