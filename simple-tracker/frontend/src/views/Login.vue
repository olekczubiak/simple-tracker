<template>
<main class="form-signin">
    <form @submit.prevent="submit">
        <h1 class="h3 mb-3 fw-normal">Zaloguj sie!</h1>

        <input v-model="data.email" class="form-control" placeholder="name@example.com" required>
        
        <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>

        <router-link class="register-router" to="/register"> Zarejestuj sie! </router-link>
    </form>
</main>
</template>

<script lang="ts">
import {reactive} from 'vue';
import {useRouter} from "vue-router";

export default {
    name: "Login",
    setup() {
        const data = reactive({
        email: '',
        password: ''
        });
        const router = useRouter();
        const submit = async () => {
        await fetch('http://localhost:8000/token', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            credentials: 'include',
            body: 'grant_type=&username=' + data.email + '&password=' + data.password + '&scope=&client_id=&client_secret='
        })
        .then(resp => {resp.json()
        .then(resp => {
            // console.log('access token')
            // console.log(resp['access_token'])
            localStorage.setItem('user-token', resp['access_token'])
        }
        )
        })
        .catch(err => {
            localStorage.removeItem('user-token')
            // console.log('blad logowania')
        })
        await router.push('/');
        }
        return {
        data,
        submit
        }
    }
}
</script>

<style>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-top: 5px;
  margin-bottom: 5px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-top: 5px;
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.register-router{
    text-justify: center;

}

</style>