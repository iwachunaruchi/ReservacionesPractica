<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";  
  import { RouterLink } from "vue-router";
  import { auth } from "@/stores/auth/auth";
  const username = ref("");
  const email = ref("");
  const password = ref("");
  const router = useRouter();
  const authStore = auth();
  const handleRegister = async () => {
    if (!username.value || !email.value || !password.value) {
      alert("Por favor, completa todos los campos.");
      return;
    }
    const response = await authStore.register(username.value, email.value, password.value);
    if(response == true){
        router.push("/");
    }
  };
</script>
<template>
    <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
      <div class="card p-4 shadow" style="width: 24rem;">
        <img loading="lazy" src="../../assets/logo_n.png"  sizes="(max-width: 300px) 100vw, 300px" class="w-100 edit_image" style="height: 256px; object-fit: cover" alt="">
        <h3 class="text-center mb-4">Registro de Usuario</h3>
        <form @submit.prevent="handleRegister">
          <div class="mb-3">
            <label for="username" class="form-label">Nombre de Usuario</label>
            <input
              type="text"
              id="username"
              class="form-control"
              v-model="username"
              placeholder="Ingresa tu usuario"
              required
            />
          </div>
          
          <div class="mb-3">
            <label for="email" class="form-label">Correo Electrónico</label>
            <input
              type="email"
              id="email"
              class="form-control"
              v-model="email"
              placeholder="Ingresa tu correo"
              required
            />
          </div>
  
          <!-- Password -->
          <div class="mb-3">
            <label for="password" class="form-label">Contraseña</label>
            <input
              type="password"
              id="password"
              class="form-control"
              v-model="password"
              placeholder="Ingresa tu contraseña"
              required
            />
          </div>
          
          <!-- Botón de Registro -->
          <div class="d-grid">
            <button type="submit" class="btn btn-primary">Registrar</button>
          </div>
        </form>
        <div class="text-center mt-3">
            ya tienes cuenta?  Puedes 
            <RouterLink to="login" class="text-decoration-none">
                iniciar sesion
            </RouterLink>
        </div>
      </div>
    </div>
  </template>
  
  <style>
  /* Estilo opcional */
  body {
    background-color: #f8f9fa;
  }
  
  .card {
    border-radius: 10px;
  }
  </style>
  