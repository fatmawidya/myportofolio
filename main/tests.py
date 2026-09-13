from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Education

class MainTest(TestCase):
    def setUp(self):
        # Data dummy Experience
        self.experience = Experience.objects.create(
            title="Open House Fasilkom UI 2024",
            description="Staff of Public Relations and Event Host.",
            category="volunteer", 
            started_at=timezone.now().date()
        )
        # Data dummy Education 
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="bachelor",
            field_of_study="Information Systems",
            start_year=2025
        )

    # --- TEST MAIN / PROFILE ---
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")
        self.assertEqual(response.status_code, 404)

    # --- TEST EXPERIENCE ---
    def test_experience_model(self):
        # Cek __str__ dan nilai category
        self.assertEqual(str(self.experience), "Open House Fasilkom UI 2024")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Volunteer")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        
        self.assertFalse(self.experience.is_ongoing)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    # --- TEST EDUCATION ---
    def test_education_model(self):
        # Cek __str__ dan data field
        self.assertEqual(str(self.education), "Universitas Indonesia - Information Systems")
        self.assertEqual(self.education.degree, "bachelor")
        self.assertEqual(self.education.start_year, 2025)
        self.assertTrue(self.education.is_current)

    def test_education_page_with_data(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "educational.html")
        self.assertContains(response, self.education.institution)
        self.assertContains(response, self.education.field_of_study)
        self.assertContains(response, "2025")

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "educational.html")
        self.assertContains(response, "No education has been added yet.")