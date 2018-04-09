--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: addresses; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.addresses (
    address_id integer NOT NULL,
    market_id integer,
    address_street character varying(64) NOT NULL,
    address_city character varying(32) NOT NULL,
    address_state character varying(32) NOT NULL,
    addresses_zip character varying(32) NOT NULL
);


ALTER TABLE public.addresses OWNER TO vagrant;

--
-- Name: addresses_address_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.addresses_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.addresses_address_id_seq OWNER TO vagrant;

--
-- Name: addresses_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.addresses_address_id_seq OWNED BY public.addresses.address_id;


--
-- Name: markets; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.markets (
    market_id integer NOT NULL,
    address_id integer,
    market_name character varying(64) NOT NULL,
    market_day character varying(32) NOT NULL,
    market_time time without time zone
);


ALTER TABLE public.markets OWNER TO vagrant;

--
-- Name: markets_market_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.markets_market_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.markets_market_id_seq OWNER TO vagrant;

--
-- Name: markets_market_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.markets_market_id_seq OWNED BY public.markets.market_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying(64),
    password character varying(64)
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: vendors; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.vendors (
    vendor_id integer NOT NULL,
    vendor_name character varying(64) NOT NULL,
    vendor_website character varying(250),
    vendor_commodity character varying(250) NOT NULL
);


ALTER TABLE public.vendors OWNER TO vagrant;

--
-- Name: vendors_vendor_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.vendors_vendor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vendors_vendor_id_seq OWNER TO vagrant;

--
-- Name: vendors_vendor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.vendors_vendor_id_seq OWNED BY public.vendors.vendor_id;


--
-- Name: address_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.addresses ALTER COLUMN address_id SET DEFAULT nextval('public.addresses_address_id_seq'::regclass);


--
-- Name: market_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.markets ALTER COLUMN market_id SET DEFAULT nextval('public.markets_market_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: vendor_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.vendors ALTER COLUMN vendor_id SET DEFAULT nextval('public.vendors_vendor_id_seq'::regclass);


--
-- Data for Name: addresses; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.addresses (address_id, market_id, address_street, address_city, address_state, addresses_zip) FROM stdin;
\.


--
-- Name: addresses_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.addresses_address_id_seq', 1, false);


--
-- Data for Name: markets; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.markets (market_id, address_id, market_name, market_day, market_time) FROM stdin;
2	\N	Monterey	Tuesday	\N
3	\N	Monterey	Tuesday	16:00:00
\.


--
-- Name: markets_market_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.markets_market_id_seq', 3, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, email, password) FROM stdin;
1	admin@email.com	adminpass
2	admin@email.com	adminpass
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 2, true);


--
-- Data for Name: vendors; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.vendors (vendor_id, vendor_name, vendor_website, vendor_commodity) FROM stdin;
\.


--
-- Name: vendors_vendor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.vendors_vendor_id_seq', 1, false);


--
-- Name: addresses_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (address_id);


--
-- Name: markets_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.markets
    ADD CONSTRAINT markets_pkey PRIMARY KEY (market_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: vendors_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.vendors
    ADD CONSTRAINT vendors_pkey PRIMARY KEY (vendor_id);


--
-- Name: addresses_market_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_market_id_fkey FOREIGN KEY (market_id) REFERENCES public.markets(market_id);


--
-- Name: markets_address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.markets
    ADD CONSTRAINT markets_address_id_fkey FOREIGN KEY (address_id) REFERENCES public.addresses(address_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

