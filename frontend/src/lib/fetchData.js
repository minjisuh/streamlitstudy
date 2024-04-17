const site_root = "http://localhost:8777/api";
export async function fetchData(url, method = 'GET', data = {}) {
    let url = new URL(site_root + url);
    const headers = { 'Content-Type': 'application/json' };
    let options ={};

    if (method === 'GET' && Object.keys(data).length > 0) {
        url.search = new URLSearchParams(data).toString();
    }

    switch (method) {
        case 'GET':
            options = { method };
            break;
        case 'POST':
        case 'PUT':
            options = {
                method,
                headers,
                body : JSON.stringify(data)
            };
            break;
        case 'DELETE':
            options = { method };
            break;
        default:
            throw new Error('Unsupported HTTP method');
    }
    const response = await fetch(url, options);
    return await response.json();
    
}