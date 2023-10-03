import folium
from geopy.geocoders import Nominatim


def generate_client_popup(client, user_permission) -> str:
    delete_button_html = ""
    if user_permission != 0:
        delete_button_html = f"""
            <tr>
                <td colspan="2">
                    <a class="btn btn-primary delete-button text-white" href="delete/{client.id}" role="button" style="width: 100%; background-color: #4e49e5";><i class="fa-solid fa-trash"></i> | Usuń klienta</a>
                </td>
            </tr>
        """
    
    html = f"""
    <div class="table-responsive shadow p-2 bg-body-tertiary rounded fs-5">
        <table class="table table-borderless mb-0">
            <tbody>
                <tr>
                    <th class="border-end bg-light font-weight-medium text-secondary px-4 py-3">Imię i Nazwisko</th>
                    <td>{ client.full_name }</td>
                </tr>
                <tr>
                    <th class="border-end bg-light font-weight-medium text-secondary px-4 py-3">Instalacja</th>
                    <td>{ client.installation }</td>
                </tr>
                <tr>
                    <th class="border-end bg-light font-weight-medium text-secondary px-4 py-3">Data instalacji</th>
                    <td>{ client.installation_date }</td>
                </tr>
                <tr>
                    <th class="border-end bg-light font-weight-medium text-secondary px-4 py-3">Adres</th>
                    <td>{ client.address }</td>
                </tr>
                <tr>
                    <th class="border-end bg-light font-weight-medium text-secondary px-4 py-3">Telefon</th>
                    <td>{ client.phone_number}</td>
                </tr>
                {delete_button_html}
            </tbody>
        </table>
    </div>
    """
    
    return html


def fetch_clients(Client) -> list:
    client_list = Client.objects.all()
    return client_list

def create_map(max_zoom) -> object:
    return folium.Map(min_zoom=6, max_zoom=max_zoom, location=[50.871852, 20.630608])

def create_viewers_map(Client) -> map:
    map = create_map(max_zoom=10)

    for client in fetch_clients(Client):

        client.location_latitude = round(client.location_latitude, 2)
        client.location_longitude = round(client.location_longitude, 2)
        if client.installation_type == "FW":
            folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip='Fotowoltaika', icon=folium.Icon(color="blue",icon="solar-panel", prefix='fa')).add_to(map)
            continue

        if client.installation_type == "PC": 
            folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip='Pompa Ciepła', icon=folium.Icon(color="orange",icon="fire", prefix='fa')).add_to(map)        
            continue

        if client.installation_type == "FWPC":
            folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip='Fotowoltaika i Pompa Ciepła', icon=folium.Icon(color="green",icon="house", prefix='fa')).add_to(map)
            continue

    map.fit_bounds(map.get_bounds())
    return map._repr_html_()


def create_admin_map(Client, user_permission) -> map:
    map = create_map(max_zoom=18)

    try:
        for client in fetch_clients(Client):
            # print(client.full_name)
            str_popup = generate_client_popup(client, user_permission)
            popup_html = folium.Html(str_popup, script=True, width=300)
            popup = folium.Popup(popup_html, min_width=300, max_width=300)

            try:
                if client.installation_type == "FW":
                    folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip=client.full_name, popup = popup, icon=folium.Icon(color="blue",icon="solar-panel", prefix='fa')).add_to(map)
                    continue

                if client.installation_type == "PC": 
                    folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip=client.full_name, popup = popup, icon=folium.Icon(color="orange",icon="fire", prefix='fa')).add_to(map)        
                    continue

                if client.installation_type == "FWPC":
                    folium.Marker(location=[client.location_latitude, client.location_longitude], tooltip=client.full_name, popup = popup, icon=folium.Icon(color="green",icon="house", prefix='fa')).add_to(map)
                    continue

            except:
                print(f'Problem z {client.full_name}')
                continue


    except:
        pass

    map.fit_bounds(map.get_bounds())
    return map._repr_html_()
    

