<script setup>
import { useRoute } from 'vue-router';
import { onMounted,ref, computed } from 'vue';
import { reservation } from '@/stores/reservation/reservation';
import { auth } from '@/stores/auth/auth';
const reservationStore = reservation();
const propertyId = ref('');
const pricePerDay = ref(0)
const total = ref(0);
const authStore = auth();
const calculateTotal = () => {

  if (!reservation_data.value.fecha_inicio || !reservation_data.value.fecha_fin) {
    total.value = 0; 
    return;
  }

  const start = new Date(reservation_data.value.fecha_inicio);
  const end = new Date(reservation_data.value.fecha_fin);

  if (start > end) {
    total.value = 0; // Si la fecha de inicio es posterior, no hay total válido
    alert("La fecha de inicio no puede ser mayor que la fecha de fin.");
    return;
  }

  const days = Math.ceil((end - start) / (1000 * 60 * 60 * 24)); // Calcular días
  total.value = days * set_reservation.value.precio_por_noche ; // Calcular el total
};
onMounted(async() => {
    propertyId.value = route.params.id;
    const response = await reservationStore.getUnitreservation(propertyId.value);
    set_reservation.value.id = reservationStore.reservationUnit._id_propiedad;
    set_reservation.value.name = reservationStore.reservationUnit.nombre;
    set_reservation.value.descripcion = reservationStore.reservationUnit.descripcion;
    set_reservation.value.direccion = reservationStore.reservationUnit.ubicacion;
    set_reservation.value.amenidades = reservationStore.reservationUnit.amenidades;
    set_reservation.value.disponibilidad = reservationStore.reservationUnit.disponibilidad;
    set_reservation.value.precio_por_noche = reservationStore.reservationUnit.precio_por_noche;

});
const reservation_data = ref({
    id: propertyId.value,
    fecha_inicio: '',
    fecha_fin: '',
    precio_total: 0,
})
const set_reservation = ref({
    id:'',
    name:'',
    descripcion:'',
    direccion:'',
    amenidades:[],
    disponibilidad:'',
    precio_por_noche:0,
})
const take_reservation = async(id)=>{
    if(authStore.rol == ''){
        alert("Debes iniciar sesion para reservar");
        return;
    }
    console.log('puede pasar')
    const response = await reservationStore.updateReservationsUser(id)
}
const route = useRoute();
</script>
<template>

    <div class="container mt-4">
        <div class="row">
            <div class="col-7 edit_image_link p-2 ">
                <div id="carouselExampleDark" class="carousel carousel-dark slide bg-body-tertiary ">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active" data-bs-interval="10000">
                        <img src="../../../assets/1.jpg" class="d-block w-100 rounded" height="500" alt="...">
                        </div>
                        <div class="carousel-item" data-bs-interval="2000">
                        <img src="../../../assets/2.jpg" class="d-block w-100" height="500" alt="...">
                        </div>
                        <div class="carousel-item">
                        <img src="../../../assets/3.jpg" class="d-block w-100" height="500" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
            <div class="col-5 edit_data">
                <div class="mt-2 ms-2">
                    <div class="d-flex justify-content-between p-2">
                        <div>
                            <h2>Propiedad:</h2>
                            <p>
                                {{ set_reservation.name }}
                            </p>
                        </div>
                        <div>
                            <h3 class="text-center">Estado:</h3>
                            <p class="text-center bg-success text-light p-2 rounded-pill ">
                                {{set_reservation.disponibilidad.disponible  ? 'No Disponible' : 'Disponible'}} 
                                <i :class="set_reservation.disponibilidad.disponible ? 'bi bi-x-circle-fill ms-2' : 'bi bi-check-circle-fill ms-2'">
                                </i>  
                            </p>
                        </div>
                    </div>
                    <h2>Descripcion:</h2>
                    <p>
                        {{ set_reservation.descripcion }}
                    </p>
                    <h2>Ubicacion</h2>
                    <p>
                        {{ set_reservation.direccion.direccion  }}
                    </p>
                    <h2>Amenidades:</h2>
                    <div>
                        <span v-for="amenidad in set_reservation.amenidades"  class="bg-success p-2  me-3 rounded-pill text-white">
                            {{ amenidad }}
                        </span>
                    </div>
                </div>
                <div class="mt-4 d-flex">
                    <div class="bg-primary-subtle p-2 rounded ">
                        Precio por noche: 
                        <p>
                            ${{ reservationStore.reservationUnit.precio_por_noche }}
                        </p>
                    </div>
                    <div class="bg-secondary-subtle p-2">
                        Fecha de inicio:
                        <p>
                            <input  type="date" v-model="reservation_data.fecha_inicio"  @change="calculateTotal" >
                        </p>
                    </div>
                    <div class="bg-warning-subtle p-2">
                        Fecha de fin:
                        <p>
                            <input type="date" v-model="reservation_data.fecha_fin"  @change="calculateTotal" >
                        </p>
                    </div>
                    <div class="bg-info-subtle p-2 rounded">
                        Precio total:
                        <p>
                            ${{ total }}
                        </p>
                    </div>
                </div>
                <div @click="take_reservation(set_reservation.id)" class=" pe-auto text-center  bg-success mt-3 rounded text-light ">
                    <p class="p-3" ><a class="pe-auto no_link ">Confirmar reserva</a></p>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
.edit_image_link{
    border: 1px solid red;
    border-radius: 15px;
}
.edit_data{
    border: 1px solid red;
    border-radius: 15px;
}
.no_link {

text-decoration: none; /* Opcional: elimina el subrayado */
color: inherit; /* Opcional: hereda el color del texto */
}
</style>