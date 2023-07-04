//? Sergio Tomás Vargas Villarreal A00837196
//? https://youtu.be/WM_yEpyUjhg

#ifndef series_h
#define series_h

#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;
#include "Serie.h"
#pragma once


class Series
{
    
public:
    Series();
    void setCantidadSeries(int _cantidadSeries);
    int getCantidadSeries();

    void addSerie(Serie _serie);
    void CalculaPromedioSerie();
    void leerArchivo();
    void reporteFrecuenciasYPromedioSeries();



private:
    Serie arrSeries[100];
    int cantidadSeries;


};

#endif