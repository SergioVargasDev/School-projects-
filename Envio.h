#ifndef Envio_h
#define Envio_h
#include "Persona.h"
#include <iostream>
#include <stdio.h>
#include <string>

class Envio
{

  private: 
  //?Aquí lo que se hizo es que habrán objetos de la clase persona dentro del constructor en sí. Dnde estarán por default a menos que tú les estipules 
  //?otras cosas. 
    Persona remitente{"sexxx", "sexo", "sexo", "se" };
    Persona destinatario;
    double costoEstandar;


    public: 
      Envio();
      Envio(Persona _remitente, Persona _destinatario, double _costoEstandar);
      void setRemitente(Persona _remitente);
      void setDestinatario(Persona _destinatario);
      void setCostoEstandar(double _costoEstandar);
      Persona getRemitente();
      Persona getDestinatario();
      double getCostoEstandar();
      virtual double calculaCostoEnvio();


};


#endif