<script setup>

</script>
<template>
    <footer class="py-8 bg-primary">
        <section class="container grid md:grid-cols-3 xs:grid-cols-1 gap-10">
            <div class="">
                <NuxtImg src="../public/logo.png" class="pb-4 h-20" />
                <ul class="flex flex-col gap-2 text-neutral-200">
                    <li class="hover:text-secondary">
                        <NuxtLink>0123456</NuxtLink>
                    </li>
                    <li class="hover:text-secondary">
                        <NuxtLink>company@gmail.com</NuxtLink>
                    </li>
                </ul>
                <div class="flex items-center w-full gap-x-4 mt-4">
                    <font-awesome-icon :icon="['fab', 'facebook']"
                        class="text-neutral-200 hover:text-secondary text-2xl" />
                    <font-awesome-icon :icon="['fab', 'twitter']"
                        class="text-neutral-200 hover:text-secondary text-2xl" />
                    <font-awesome-icon :icon="['fab', 'instagram']"
                        class="text-neutral-200 hover:text-secondary text-2xl" />
                </div>
            </div>

            <div class="pt-5">
                <h1 class="text-white font-normal text-3xl pb-4 border-b border-border">Products</h1>
                <ul class="flex flex-col gap-2 mt-4 text-neutral-200">
                    <li class="hover:text-secondary">
                        <NuxtLink>0123456</NuxtLink>
                    </li>
                    <li class="hover:text-secondary">
                        <NuxtLink>company@gmail.com</NuxtLink>
                    </li>
                </ul>
            </div>

            <div class="pt-5">
                <h1 class="text-white font-normal text-3xl pb-4 border-b border-border">Products</h1>
                <ul class="flex flex-col gap-2 mt-4 text-neutral-200">
                    <li class="hover:text-secondary">
                        <NuxtLink>0123456</NuxtLink>
                    </li>
                    <li class="hover:text-secondary">
                        <NuxtLink>company@gmail.com</NuxtLink>
                    </li>
                </ul>
            </div>
        </section>
    </footer>
</template>