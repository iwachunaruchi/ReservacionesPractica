<script setup>
import { reservation } from '@/stores/reservation/reservation';
import { useRouter } from 'vue-router';
import {ref, onMounted} from 'vue';
const router = useRouter();
const reservationStore = reservation();
onMounted( async () => {
  reservationStore.getReservations();
});
const gotoDetails = (id) => {
  router.push({name: 'detalles', params: {id}});
}
</script>
<template>
    <div class="container ">
      <section>
        <div class="container py-6 py-lg-8">
            <div class="row mb-5 text-center">
                <div class="col mw-10 mx-auto">
                    <div class="lc-block mb-4">
                        <div editable="rich">
                            <h2 class="display-4 fw-bold ls-n1">Propiedades actuales</h2>
                        </div>
                    </div>
                </div>
            </div>
            <div class="lc-block">
                <div id="mygetposts" class="row g-3">
                    <div v-for="data in reservationStore.reservations" class="col-md-6 mb-5 mb-md-4 position-relative align-content-start ">
                        <div class="row g-2 place_list bg-body-tertiary p-2">
                            <div class="col-12 col-lg-4">
                                <img loading="lazy" src="../../assets/placeholder.jpg"  sizes="(max-width: 300px) 100vw, 300px" class="w-100 edit_image" style="height: 256px; object-fit: cover" alt="">
                            </div>

                            <div class="col-12 col-lg-8 ">
                              <div class="mb-3">
                                <p class="small mb-1">
                                  <span class="text-body text-opacity-50">
                                    <small v-for="amend in data.amenidades" class="text-white ms-1 bg-secondary p-1 rounded">
                                      {{ amend }}
                                    </small>
                                  </span>
                                </p>
                                <a >
                                  <h3 class="fw-bold fs-5">
                                    {{ data.nombre }}
                                  </h3>
                                </a>
                              </div>
                              <div class="hstack gap-2 align-items-center">
                                <span class="fw-semibold">
                                  <div class="mt-1">
                                    Precio por noche:
                                    <a class="bg-danger p-2 rounded-pill no_link text-white fst-italic">
                                      ${{ data.precio_por_noche }}
                                    </a>
                                  </div>
                                  <div class="mt-2">
                                    <a class="no_link">
                                      Dirección: {{ data.ubicacion.direccion }}
                                    </a>
                                  </div>
                                </span>
                              </div>
                              <div class="d-flex justify-content-end" >
                                <div >
                                  <div class="bg-success p-3 rounded-pill" @click="gotoDetails(data._id_propiedad)">
                                    <a class="no_link me-2 text-white" >{{data.disponibilidad.disponible ? 'No Disponible' : 'Disponible'}}                                    </a>
                                    <i :class="data.disponibilidad.disponible ? 'bi bi-x-circle-fill' : 'bi bi-check-circle-fill'" ></i>
                                  </div>
                                </div>
                              </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>


    </div>
</template>
<style scoped>
.no_link {
  pointer-events: none; /* Desactiva los clics */
  cursor: default; /* Cambia el cursor para mostrar que no es interactivo */
  text-decoration: none; /* Opcional: elimina el subrayado */
  color: inherit; /* Opcional: hereda el color del texto */
}
.place_list{
  border: 1px solid slategray;
  border-radius: 15px;
  box-shadow: 10px 5px 5px black;
}
.place_list:hover{
  box-shadow: 10px 5px 5px rgb(214, 97, 97);
}
.edit_image{
  border-radius: 15px;
  box-shadow: 10px 10px 10px  rgba(0, 0, 0, 0.192);
}

</style>