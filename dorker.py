U
    �Q;`  �                   @   s�   d dl Z d dlZd dlZzd dlZd dlZW n( ek
rT   e�d� e�d� Y nX d dlmZ d dlmZm	Z	m
Z
 e
ZeZejZejZejZejZejZe� d�Ze� d�Zdd	� Ze�d
� dZe�  dd� Ze�  dS )�    Nzpip install googlesearchzpip install colorama)�search)�Fore�Back�Stylez!|                               |z!=================================c                   C   s0   t t� tj� dt� dt� dt� dt� d�� d S )Nzr   
|                               |
|===============================|
|-------------------------------|
~~~~~[+]zBy: Anikin Lukez[+]~~~~~~
            ZDORKERz�       

|-------------------------------|
|===============================|
|                               |
|                               |)�print�y�sZBRIGHT�r�c� r   r   �dork.py�banner   s
    �
�r   �clear� c               	      s:  z�t t� dt� dt� d��} t t� dt� dt� d��}t t� dt� dt� d��� tt� tt� � fdd�}d}d}t| d	d
t|�dd dd�D ]P}|d }tt� |� t	�
d� |d7 }|t|�kr� q�|}||� t	�
d� q�W n: tk
�r   tdt� d�� t	�
d� t�d� Y nX tdt� d�� t��  d S )N�|z  [!]Enter a Dork:� z  [!]Enter Amount Value:z  [!]Output file name:c                    s2   t � d d�}|�t| �� |�d� |��  d S )Nz.txt�a�
)�open�write�str�close)�user�file��logr   r   �logger0   s    
zdorks.<locals>.loggerr   ZcomZen�   )ZtldZlangZnum�start�stop�pause�   g�������?r   z![x] User Interruption Detected..!g      �?u   [✅️] Complete!!)�inputr   �gr   �line�line2r   �intr
   �time�sleep�KeyboardInterruptr	   �sys�exit)ZdorkZamountr   Zrequ�flagZresultsr   r   r   r   �dorks)   s2    

r-   )r'   �osr*   ZgooglesearchZcolorama�ImportError�systemr   r   r   r   r   �fZREDr	   ZGREENr#   ZYELLOWr   ZBLUE�bZCYANr
   r$   r%   r   r   r-   r   r   r   r   �<module>   s.   



'