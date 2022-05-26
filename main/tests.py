import pytest
from daycare.models import DayCare


@pytest.mark.django_db
class TestAboutView:
    def test_redirected_to_about_section(self, client):
        response = client.get('/about')
        assert response.status_code == 301
        response = client.get(response.url)
        assert response.status_code == 200


@pytest.mark.django_db
class TestLoginView:
    def test_enter_login_page(self, client):
        response = client.get('/login/')
        assert response.status_code == 200

    def test_valid_login_daycare_user_info(self, client, create_daycare_user, daycare_data):
        previous_logged_user = client.get('/').wsgi_request.user
        form = {'username': pytest.DAYCARE_USERNAME,
                'password': pytest.DAYCARE_PASSWORD,
                }

        response = client.post('/login/', form, follow=True)
        current_log_user = response.wsgi_request.user
        assert current_log_user == create_daycare_user.user
        assert previous_logged_user != current_log_user

    def test_invalid_login_daycare_user_info(self, client):
        form = {'username': "daycare@address.com",
                'password': "incorrect",
                }
        response = client.post('/login/', form, follow=True)
        assert response.wsgi_request.user.is_anonymous

    def test_block_logged_user_from_login_page(self, client, create_dog_owner_user):
        client.force_login(user=create_dog_owner_user.user)
        response = client.get("/login/")
        assert response['Location'] == '/'


@pytest.mark.django_db
class TestLogoutView:
    def test_successful_logout(self, client, create_dog_owner_user):
        client.force_login(user=create_dog_owner_user.user)
        logged_user = client.get('/').wsgi_request.user
        response = client.get('/logout/')
        assert response['Location'] == '/login/'
        assert response.wsgi_request.user != logged_user


@pytest.mark.django_db
class TestIndexView:
    def test_root_entrypoint_redirection_unlogged_user(self, client):
        response = client.get("/")
        assert response.status_code == 302
        assert response['Location'] == '/login/'

    def test_root_entrypoint_redirection_logged_daycare_user(self, client, create_daycare_user):
        client.force_login(user=create_daycare_user.user)
        response = client.get("/")
        assert response.status_code == 302
        assert response['Location'] == '/homepage/'


@pytest.mark.django_db
class TestHomepageView:
    def test_unlogged_user_access_to_homepage(self, client):
        response = client.get("/homepage/")
        assert response.status_code == 302
        assert response['Location'] == '/login/?next=/homepage/'

    def test_dog_owner_homepage_is_visible_for_dog_owner(self, client, create_dog_owner_user):
        client.force_login(user=create_dog_owner_user.user)
        response = client.get("/homepage/")
        assert response.status_code == 200
        list_of_daycares_from_response = list(response.context['daycares'])
        list_of_all_daycares = list(DayCare.objects.all())
        assert list_of_daycares_from_response == list_of_all_daycares


@pytest.mark.django_db
class TestNavbarView:
    def test_navbar_getting_dog_owner_nickname_and_profile_picture(self, client, create_dog_owner_user):
        client.force_login(user=create_dog_owner_user.user)
        response = client.get("/homepage/")
        dog_owner_picture_url = create_dog_owner_user.dog_picture_url
        assert response.context['navbar_picture_url'] == dog_owner_picture_url
        dog_owner_name = create_dog_owner_user.__str__()
        assert response.context['navbar_name'] == dog_owner_name

    def test_navbar_getting_daycare_nickname_and_profile_picture(self, client, create_daycare_user):
        client.force_login(user=create_daycare_user.user)
        response = client.get("/homepage/")
        daycare_name = create_daycare_user.name
        assert response.context['navbar_name'] == daycare_name
        daycare_primary_image_url = create_daycare_user.get_daycare_primary_image_url()
        assert response.context['navbar_picture_url'] == daycare_primary_image_url
