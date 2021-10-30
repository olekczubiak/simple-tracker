<template>
  <form @submit.prevent="submit">
        <h1 class="h3 mb-3 fw-normal">Zarejestruj sie!</h1>

        <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com" required>

        <input v-model="data.company" class="form-control" placeholder="company">

        <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Submit</button>

    </form>
</template>

<script lang="ts">
import {reactive} from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'Register',
    setup() {
      const data = reactive({
      id: 0,
      email: '',
      password: '',
      is_active: true,
      company: '',
    });
      const router = useRouter();

      const submit = async () => {
        await fetch('http://localhost:8000/user/create', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(data)
        });

        await router.push('/login');
      }

      return {
        data,
        submit
      }
    }
}
</script>
