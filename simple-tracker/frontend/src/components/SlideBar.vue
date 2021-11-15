<template>
<nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
<div class="position-sticky pt-3">
    <ul class="nav flex-column">
    <li class="nav-item">
        <router-link to="/panel" class="nav-link">
        <span data-feather="shopping-cart"></span>
        Panel main page
        </router-link>
    </li>
    <li class="nav-item">
        <router-link to="/panel/monitor" class="nav-link" aria-current="page">
        <span data-feather="home"></span>
        Monitorowanie
        </router-link>
    </li>
    <li class="nav-item">
        <router-link to="/panel/analysis" class="nav-link">
        <span data-feather="file"></span>
        Analiza
        </router-link>
    </li>
    </ul>

    <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
    <span>Historia</span>
    <a class="link-secondary" href="#" aria-label="Add a new report">
        <span data-feather="plus-circle"></span>
    </a>
    </h6>
    <ul class="nav flex-column mb-2">
    <li class="nav-item">
        <router-link to="/panel/calendar" class="nav-link">
        <span data-feather="file-text"></span>
        Kalendarz
        </router-link>
    </li>
    </ul>

    <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
    <span>Akcje</span>
    <a class="link-secondary" href="#" aria-label="Add a new report">
        <span data-feather="plus-circle"></span>
    </a>
    </h6>
    <ul class="nav flex-column mb-2">
    <li v-if="isLogin==false" class="nav-item">
        <router-link class="nav-link" to="/login">
        <span data-feather="file-text"></span>
        Zaloguj!
        </router-link>
    </li>
    <li v-if="isLogin==true" class="nav-item">
        <a v-on:click="logoutButton" class="nav-link">
        <span data-feather="file-text"></span>
        Wyloguj!
        </a>
    </li>
    </ul>
</div>
</nav>
</template>

<script>
export default {
    name: 'slideBar',
    data() {
        return {
            isLogin: Boolean,
        }
    },
    created() {
        const myToken = localStorage.getItem('user-token');
        if (myToken == null) {
            this.isLogin = false
        } else {
            this.isLogin = true
        }
    },
    methods: {
        logoutButton() {
            localStorage.removeItem('user-token');
            window.location.reload();
        }
    }
}
</script>

<style>
/*
* Sidebar
*/

.sidebar {
position: fixed;
top: 0;
/* rtl:raw:
right: 0;
*/
bottom: 0;
/* rtl:remove */
left: 0;
z-index: 100; /* Behind the navbar */
padding: 48px 0 0; /* Height of navbar */
box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

@media (max-width: 767.98px) {
.sidebar {
    top: 5rem;
}
}

.sidebar-sticky {
position: relative;
top: 0;
height: calc(100vh - 48px);
padding-top: .5rem;
overflow-x: hidden;
overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

.sidebar .nav-link {
font-weight: 500;
color: #333;
}

.sidebar .nav-link .feather {
margin-right: 4px;
color: #727272;
}

.sidebar .nav-link.active {
color: #2470dc;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
color: inherit;
}

.sidebar-heading {
font-size: .75rem;
text-transform: uppercase;
}
</style>