PGDMP     5                
    z            DataRestoran    14.2    14.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    40973    DataRestoran    DATABASE     n   CREATE DATABASE "DataRestoran" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_Indonesia.1252';
    DROP DATABASE "DataRestoran";
                postgres    false            �            1259    40992    datamenurestoran    TABLE     �   CREATE TABLE public.datamenurestoran (
    id_barang integer NOT NULL,
    nama_barang character varying(25) DEFAULT NULL::character varying,
    deskripsi_barang character varying(50) DEFAULT NULL::character varying,
    harga_barang double precision
);
 $   DROP TABLE public.datamenurestoran;
       public         heap    postgres    false            �            1259    40999    datapesanancustomer    TABLE     �   CREATE TABLE public.datapesanancustomer (
    id_barang integer NOT NULL,
    jumlah_barang integer,
    nama_barang character varying(50) DEFAULT NULL::character varying,
    harga_barang double precision,
    total_harga double precision
);
 '   DROP TABLE public.datapesanancustomer;
       public         heap    postgres    false            �          0    40992    datamenurestoran 
   TABLE DATA           b   COPY public.datamenurestoran (id_barang, nama_barang, deskripsi_barang, harga_barang) FROM stdin;
    public          postgres    false    209   <       �          0    40999    datapesanancustomer 
   TABLE DATA           o   COPY public.datapesanancustomer (id_barang, jumlah_barang, nama_barang, harga_barang, total_harga) FROM stdin;
    public          postgres    false    210          c           2606    40998 &   datamenurestoran datamenurestoran_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.datamenurestoran
    ADD CONSTRAINT datamenurestoran_pkey PRIMARY KEY (id_barang);
 P   ALTER TABLE ONLY public.datamenurestoran DROP CONSTRAINT datamenurestoran_pkey;
       public            postgres    false    209            e           2606    41004 ,   datapesanancustomer datapesanancustomer_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.datapesanancustomer
    ADD CONSTRAINT datapesanancustomer_pkey PRIMARY KEY (id_barang);
 V   ALTER TABLE ONLY public.datapesanancustomer DROP CONSTRAINT datapesanancustomer_pkey;
       public            postgres    false    210            f           2606    41005 .   datapesanancustomer datapesanancustomer_ibfk_1    FK CONSTRAINT     �   ALTER TABLE ONLY public.datapesanancustomer
    ADD CONSTRAINT datapesanancustomer_ibfk_1 FOREIGN KEY (id_barang) REFERENCES public.datamenurestoran(id_barang);
 X   ALTER TABLE ONLY public.datapesanancustomer DROP CONSTRAINT datapesanancustomer_ibfk_1;
       public          postgres    false    209    3171    210            �   �   x�u�;�0Dk�{	�#�(��Y�Ub;��
q{�8 ���/�����ȶ�y��E���C��à@�-x~j/&�Z�eYTY:k#鞳$'��'�7=i��d�ٸ(�s�HG���'��߉�8S'����B�O�=)v��*)+����T:���eɃ���N�z"�A��<%��h���ȇߙ��(�I�Ί�x֎s�      �      x������ � �     