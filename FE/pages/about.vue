<script setup>
import { EnvelopeIcon, MapIcon, MapPinIcon, PhoneArrowDownLeftIcon } from '@heroicons/vue/24/outline';


</script>
<template>
    <section class="py-20 bg-background">
        <h1 class="text-6xl text-center font-black">Contact Us</h1>
    </section>

    <section class="py-20 flex flex-col gap-8">
        <div class="container flex gap-8">
            <div class="flex-1">
                <form class="flex flex-col">
                    <div class="flex mb-8 gap-4">
                        <input placeholder="Email"
                            class="bg-background text-gray-200 border-0 rounded-lg p-2 w-1/2 focus:bg-primary focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
                            type="email" />
                        <input placeholder="Phone"
                            class="bg-background text-gray-200 border-0 rounded-lg p-2 w-1/2 focus:bg-primary focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
                            type="tel" />
                    </div>
                    <input placeholder="Name"
                        class="bg-background text-gray-200 border-0 rounded-lg p-2 focus:bg-primary focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150"
                        type="text" />
                    <button class="backdrop-blur-md lg:font-bold text-text
                    isolation-auto before:absolute before:w-full before:transition-all before:duration-700
                    before:hover:w-full before:-top-1/2 before:-left-full before:hover:left-0 before:rounded-full before:bg-secondary
                    hover:text-white before:-z-10 before:aspect-square before:hover:scale-150 before:hover:duration-700
                    relative z-10 py-2 px-4 mt-8 w-1/2 overflow-hidden border border-border rounded-lg" type="submit">
                        Submit
                    </button>
                </form>
            </div>
            <div class="flex-1 grid grid-cols-2 gap-4">
                <div class="p-8 flex flex-col items-center justify-center gap-6 border border-border rounded-xl">
                    <div class="flex gap-4 justify-center">
                        <PhoneArrowDownLeftIcon class="w-6 h-6" />
                        <h1 class="font-bold text-xl">012345678</h1>
                    </div>
                    <p class="text-base text-center">Foot touch flushsdvasdvasdvasv</p>
                </div>
                <div class="p-8 flex flex-col items-center justify-center gap-6 border border-border rounded-xl">
                    <div class="flex gap-4 justify-center">
                        <EnvelopeIcon class="w-6 h-6" />
                        <h1 class="font-bold text-xl">012345678</h1>
                    </div>
                    <p class="text-base text-center">Foot touch flushsdvasdvasdvasv</p>
                </div>
                <div
                    class="col-span-2 p-8 flex flex-col items-center justify-center gap-6 border border-border rounded-xl">
                    <div class="flex gap-4 justify-center">
                        <MapPinIcon class="w-6 h-6" />
                        <h1 class="font-bold text-xl">012345678</h1>
                    </div>
                    <p class="text-base text-center">Foot touch flushsdvasdvasdvasv</p>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="relative text-right w-full h-[400px]">
                <div class="overflow-hidden bg-none w-full h-[400px]"><iframe class="w-full h-[400px]" frameborder="0"
                        scrolling="no" marginheight="0" marginwidth="0"
                        src="https://maps.google.com/maps?width=600&height=400&hl=en&q=University%20of%20Oxford&t=&z=14&ie=UTF8&iwloc=B&output=embed"></iframe><a
                        href="https://sprunkiretake.net"
                        style="font-size:2px!important;color:gray!important;position:absolute;bottom:0;left:0;z-index:1;max-height:1px;overflow:hidden">sprunki
                        retake</a></div>
            </div>
        </div>
    </section>
</template>