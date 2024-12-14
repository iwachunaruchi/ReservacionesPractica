import { defineStore } from 'pinia'
import { apiClient } from '@/utils/apiClient';

export const auth = defineStore('autenticado', {
  state: () => ({
    rol:'',
    session:'',
    user:''
  }),
  actions:{
    async login(username, password){
      try {
        const response = await apiClient.post('/auth/login/login', {username, password});
        console.log(response);
        this.rol = response.rol;
        this.session = response.token;
        this.user = response.username;
        return true
      }catch(error){
        console.log(error);
        return false
      }
    },
    async logout(){
      try{
        const response = await apiClient.post('/auth/login/logout')
        this.rol = '';
        this.session = '';
      }catch(error){
        console.log(error);
      }
    },
    async register(username, password, email){
      try {
        const response = await apiClient.post('/auth/register/register', {username, password, email});
        this.login(username, password)
        console.log(response);
        return true
      } catch (error) {
        return false
      }
    }
  }
})
  