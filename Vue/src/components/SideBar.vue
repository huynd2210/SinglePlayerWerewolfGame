<template>
    <aside :class="`${bExpanded && 'is-expanded'}`">
        <div class="main">
            <span class="material-symbols-outlined">
            sports_esports
            </span>
        </div>

        <div class="menu-toggle-wrap">
            <button class="menu-toggle" @click="ToggleMenu">
                <span class="material-symbols-outlined">
                    keyboard_double_arrow_right
                </span>
            </button>
        </div>

        <h3>Menu</h3>
        <div class="menu">
            <router-link class="button" to="/">
                <span class="material-symbols-outlined">home</span>
                <span class="text">Home</span>
            </router-link>
            <router-link class="button" to="/chat">
                <span class="material-symbols-outlined">chat</span>
                <span class="text">History</span>
            </router-link>
            <router-link class="button" to="/notes">
                <span class="material-symbols-outlined">assignment</span>
                <span class="text">Notes</span>
            </router-link>
        </div>

        <div class="flex"></div>

        <div class="menu">
            <router-link class="button" to="/settings">
                <span class="material-symbols-outlined">settings</span>
                <span class="text">Settings</span>
            </router-link>
        </div>
    </aside>
</template>

<script setup>
import { ref } from 'vue'

const bExpanded = ref(localStorage.getItem("bMenuExpanded") === "true")

const ToggleMenu = () => {
    bExpanded.value = !bExpanded.value
    localStorage.setItem("bMenuExpanded", bExpanded.value)
}

</script>

<style lang="scss" scoped>
aside {
    display: flex;
    flex-direction: column;
    width: calc(2rem + 32px);

    overflow: hidden;
    min-height: 100vh;
    padding: 1rem;

    background-color: var(--dark);
    color: var(--light);

    transition: 0.2s ease-out;

    .flex {
        flex: 1 1 0;
    }
    .material-symbols-outlined {
        margin-bottom: 1rem;
        font-size: 2rem;
    }

    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 1rem;

        position: relative;
        top: 0;
        transition: 0.2s ease-out;
        
        .flex {
            flex: 1 1 0;
        }
        .menu-toggle {
            transition: 0.2s ease-out;

            .material-symbols-outlined {
                font-size: 2rem;
                color: var(--light);
                transition: 0.2s ease-out;
            }

            &:hover {
                .material-symbols-outlined {
                    color: var(--primary);
                    transform: translateX(0.5rem);
                }
            }
        }
    }

    .button .text{
        opacity: 0;
        transition: 0.3s ease-out;
    }

    h3 {
        opacity: 0;
        color: var(--grey);
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        transition: 0.3s ease-out;
    }

    .menu {
        margin: 0 -1rem;

        .button {
            display: flex;
            align-items: center;
            text-decoration: none;

            padding-left: 1rem;
            transition: 0.2s ease-out;

            .material-symbols-outlined {
                font-size: 2rem;
                color: var(--light);
                padding-top: 0.5rem;
                transition: 0.2s ease-out;
            }

            .text {
                color: var(--light);
                transition: 0.2s ease-out;
            }

            &:hover, &.router-link-exact-active {
                background-color: var(--dark-alt);

                .material-symbols-outlined, .text {
                    color: var(--primary);
                }
            }

            &.router-link-exact-active {
                border-right: 5px solid var(--primary);
            }
        }
    }

    &.is-expanded {
        width: var(--sidebar-width);

        .menu-toggle-wrap {
            top: -4rem;
            .menu-toggle {
                transform: rotate(-180deg);
            }
        }

        h3 {
            opacity: 1;
        }

        .menu {
            .button .text{
                opacity: 1;
            }
            .button {
                .material-symbols-outlined {
                    margin-right: 1rem;
                }
            }
        }

        
    }

    @media (max-width: 768px) {
        position: fixed;
        z-index: 99;
    }
}
</style>