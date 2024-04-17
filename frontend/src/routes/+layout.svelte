<script>
    import "../app.pcss";
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { fetchData } from '$lib/fetchData.js';

</script>
<Navbar>
    <NavBrand href="/">
        <img src="images/logo.png" class="me-3 h-6 sm:h-9" alt="Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Logo</span>
    </NavBrand>
    <NavHamburger />
    <NavUl>
        <NavLi href="/">Home</NavLi>
        <NavLi href="/about">About</NavLi>
    </NavUl>
</Navbar>
<div class="px-2 sm:px-4"><div class="container mx-auto">
<slot></slot>
</div></div>
<div>
    {#await fetchData("add", "GET", {a: 1, b: 3})}
    <b>Loading...</b>
    {:then data}
    <b>{data.result}</b>
    {/await}

</div>