import { defineStore } from 'pinia'
import { apiClient } from '@/utils/apiClient';
export const reservation = defineStore('reservacion', {
    state: () => ({
      reservations: [], // Lista de reservas
      loading: false,   // Indicador de carga
      error: null,      // Almacena errores de las solicitudes
      reservationUnit: [],
    }),
    actions:{
      async getReservations() {
        this.loading = true;
        this.error = null;
        try {
          const response = await apiClient.get('/api/properties');
          console.log(response);
          this.reservations = response;
        } catch (error) {
          console.log(error);
        }
      },
      async getUnitreservation(id){
        this.loading = true;
        this.error = null;
        try {
          const response = await apiClient.get(`/api/properties/${id}`);
          this.reservationUnit = response;
          return this.reservationUnit;
          console.log(this.reservationUnit);
        } catch (error) {
          
        }
      },
      async updateReservationsUser(id){
        try {
          const response = await apiClient.post(`/api/availability/${id}`)
          this.getReservations();
        } catch (error) {
          
        }
      }
    }
  })
  