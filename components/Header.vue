<script setup></script>
<template>
    <header class="py-4 border-b bg-white sticky top-0 z-30 opacity-80">
        <nav class="flex container items-center">
            <NuxtLink to="/" class="flex gap-1 items-center">
                <NuxtImg width="160px" densities="x1" format="webp" alt="logo" src="../public/logo.png"></NuxtImg>
            </NuxtLink>
            <ul class="flex gap-10 ml-auto text-lg text-text">
                <li class="hover:text-secondary hover:font-semibold">
                    <NuxtLink to="/">Home</NuxtLink>
                </li>
                <li class="hover:text-secondary hover:font-semibold">
                    <NuxtLink to="/products">Products</NuxtLink>
                </li>
                <li class="hover:text-secondary hover:font-semibold">
                    <NuxtLink to="/blog">Blog</NuxtLink>
                </li>
                <li class="hover:text-secondary hover:font-semibold">
                    <NuxtLink to="/about">About</NuxtLink>
                </li>
            </ul>
        </nav>
    </header>
</template>