#!/usr/bin/env python
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserAccount

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()


class UserAccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserAccount.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser',
            first_name='Test',
            last_name='User',
            agreed=True,
        )
        self.admin_user = UserAccount.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
            username='adminuser',
            first_name='Admin',
            last_name='User',
            agreed=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """Test creating a new user"""
        payload = {
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'agreed': True,
        }
        res = self.client.post(reverse('user-list'), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = UserAccount.objects.get(id=res.data['id'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_invalid(self):
        """Test creating a new user with invalid payload"""
        payload = {
            'email': '',
            'password': '',
            'username': '',
            'first_name': '',
            'last_name': '',
            'agreed': False,
        }
        res = self.client.post(reverse('user-list'), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        payload = {
            'email': 'newadmin@example.com',
            'password': 'newadminpass123',
            'username': 'newadminuser',
            'first_name': 'New',
            'last_name': 'Admin',
            'agreed': True,
        }
        self.client.force_authenticate(user=self.admin_user)
        res = self.client.post(reverse('user-list'), payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = UserAccount.objects.get(id=res.data['id'])
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser_invalid(self):
        """Test creating a new superuser with invalid payload"""
        payload = {
            'email': '',
            'password': '',
            'username': '',
            'first_name': '',
            'last_name': '',
            'agreed': False,
        }
        self.client.force_authenticate(user=self.admin_user)
        res = self.client.post(reverse('user-list'), payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_users(self):
        """Test listing all users"""
        res = self.client.get(reverse('user-list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_retrieve_user(self):
        """Test retrieving a user"""
        res = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], self.user.email)

    def test_update_user(self):
        """Test updating a user"""
        payload = {
            'first_name': 'Updated',
            'last_name': 'User',
        }
        res = self.client.patch(reverse('user-detail', args=[self.user.id]), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['first_name'], payload['first_name'])

    def test_delete_user(self):
        """Test deleting a user"""
        res = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(UserAccount.objects.filter(id=self.user.id).exists())