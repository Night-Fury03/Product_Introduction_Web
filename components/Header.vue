<script setup lang="ts" ></script>
<template>
    <header class="py-4 border-b">
        <nav class="flex container items-center">
            <NuxtLink to="/" class="flex gap-1 items-center">
                <span>Logo</span>
            </NuxtLink>
            <ul class="flex gap-6 ml-auto text-xl font-bold capitalize">
                <li>
                    <NuxtLink to="/">Home</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/products">Products</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/blog">Blog</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/about">About</NuxtLink>
                </li>
            </ul>
        </nav>
    </header>
</template>